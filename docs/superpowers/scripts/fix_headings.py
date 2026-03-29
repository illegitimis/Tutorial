#!/usr/bin/env python3
"""Fix heading casing to American English title case in markdown files."""

import re
import os
import sys

SMALL_WORDS = {
    'a', 'an', 'the',
    'and', 'but', 'or', 'nor',
    'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'as', 'up',
    'vs', 'vs.'
}

# Technical terms that must retain exact casing (key: lowercase, value: correct form)
TECH_TERMS = {
    'asp.net': 'ASP.NET',
    'ef': 'EF',
    'graphql': 'GraphQL',
    'nunit': 'NUnit',
    'xunit': 'xUnit',
    'tpl': 'TPL',
    'clr': 'CLR',
    'acid': 'ACID',
    'solid': 'SOLID',
    'cqrs': 'CQRS',
    'rest': 'REST',
    'http': 'HTTP',
    'https': 'HTTPS',
    'api': 'API',
    'mvc': 'MVC',
    'git': 'Git',
    'github': 'GitHub',
    'npm': 'NPM',
    'pwa': 'PWA',
    'css': 'CSS',
    'html': 'HTML',
    'toc': 'TOC',
    'js': 'JS',
    'url': 'URL',
    'ui': 'UI',
    'wpf': 'WPF',
    'uml': 'UML',
    'orm': 'ORM',
    'oop': 'OOP',
    'sql': 'SQL',
    'nosql': 'NoSQL',
    'yaml': 'YAML',
    'json': 'JSON',
    'xml': 'XML',
    'di': 'DI',
    'ioc': 'IoC',
    'ddd': 'DDD',
    'dto': 'DTO',
    'dao': 'DAO',
    'mongodb': 'MongoDB',
    'mongo': 'Mongo',
    'mysql': 'MySQL',
    'kafka': 'Kafka',
    'docker': 'Docker',
    'linq': 'LINQ',
    'azure': 'Azure',
    'nuget': 'NuGet',
    'signalr': 'SignalR',
    'zeromq': 'ZeroMQ',
    'angularjs': 'AngularJS',
    'angular': 'Angular',
    'bootstrap': 'Bootstrap',
    'webpack': 'webpack',
    'redux': 'Redux',
    'rx': 'Rx',
    'winforms': 'WinForms',
    'postsharp': 'PostSharp',
    'swagger': 'Swagger',
    'hateoas': 'HATEOAS',
    'etag': 'ETag',
    'devops': 'DevOps',
    'saml': 'SAML',
    'oauth': 'OAuth',
    'oidc': 'OIDC',
    'jwt': 'JWT',
    'mfa': 'MFA',
    'sso': 'SSO',
    'rbac': 'RBAC',
    'iam': 'IAM',
    'ddos': 'DDoS',
    'nsg': 'NSG',
    'vpn': 'VPN',
    'vm': 'VM',
    'vnet': 'VNet',
    'sla': 'SLA',
    'tco': 'TCO',
    'iot': 'IoT',
    'ai': 'AI',
    'ml': 'ML',
    'dns': 'DNS',
    'cdn': 'CDN',
    'ssl': 'SSL',
    'tls': 'TLS',
    'nat': 'NAT',
    'osi': 'OSI',
    'smtp': 'SMTP',
    'tcp': 'TCP',
    'udp': 'UDP',
    'ip': 'IP',
    'ftp': 'FTP',
    'ssh': 'SSH',
    'sftp': 'SFTP',
    '.net': '.NET',
    'autorest': 'AutoRest',
    'automapper': 'AutoMapper',
    'httpclient': 'HttpClient',
    'priming': 'Priming',
    'primeng': 'PrimeNG',
    'netmq': 'NetMQ',
    'gridfs': 'GridFS',
    'cosmos': 'Cosmos',
    'tigergraph': 'TigerGraph',
    'neo4j': 'Neo4j',
    'postgresql': 'PostgreSQL',
    'postgre': 'PostgreSQL',
    'mssql': 'MSSQL',
    'tempdb': 'TempDB',
    'nginx': 'Nginx',
    'linux': 'Linux',
    'az-900': 'AZ-900',
    'blazor': 'Blazor',
    'nginx': 'Nginx',
    'redis': 'Redis',
    'msft': 'MSFT',
    'az900': 'AZ-900',
    'faqs': 'FAQs',
    'faq': 'FAQ',
}


def title_case_word(word, is_first, is_last):
    """Apply title case rules to a single word."""
    # Preserve words that are already mixed-case or all-caps (likely already correct)
    stripped = word.strip('.,;:!?()"\'*[]#/-')
    stripped_lower = stripped.lower()

    # Check for tech terms exact match
    if stripped_lower in TECH_TERMS:
        tech = TECH_TERMS[stripped_lower]
        return word.replace(stripped, tech)

    if is_first or is_last:
        # Capitalize first letter
        if word and word[0].islower():
            return word[0].upper() + word[1:]
        return word
    elif stripped_lower in SMALL_WORDS:
        return word.lower()
    else:
        # Capitalize first letter if not already
        if word and word[0].islower():
            return word[0].upper() + word[1:]
        return word


def title_case_heading(text):
    """Convert heading text to title case. Returns None if heading should not be changed."""
    # Don't touch headings that contain inline code (backticks)
    if '`' in text:
        return None
    # Don't touch headings that look like code comments (start with #)
    # These are already handled by the regex not matching inline # in code blocks

    words = text.split()
    if not words:
        return text

    result = []
    for i, word in enumerate(words):
        is_first = (i == 0)
        is_last = (i == len(words) - 1)
        result.append(title_case_word(word, is_first, is_last))

    return ' '.join(result)


def is_already_title_case(text):
    """Check if heading is already in acceptable title case (no change needed)."""
    new_text = title_case_heading(text)
    return new_text is None or new_text == text


def fix_file_headings(filepath):
    """Fix headings in a single file. Returns count of changes made."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_code_block = False
    new_lines = []
    changes = 0

    for line in lines:
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block

        if not in_code_block:
            m = re.match(r'^(#{1,3}) (.+)(\s*)$', line)
            if m:
                prefix = m.group(1)
                heading_text = m.group(2)
                trailing = m.group(3)

                new_text = title_case_heading(heading_text)
                if new_text is not None and new_text != heading_text:
                    new_line = f'{prefix} {new_text}{trailing}'
                    new_lines.append(new_line)
                    changes += 1
                    print(f'  [{filepath}] {prefix} {heading_text!r} -> {new_text!r}')
                    continue

        new_lines.append(line)

    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    return changes


def process_directories(dirs):
    """Process all .md files in given directories."""
    total = 0
    for d in dirs:
        for root, _, files in os.walk(d):
            for fname in files:
                if fname.endswith('.md'):
                    path = os.path.join(root, fname)
                    count = fix_file_headings(path)
                    total += count
    return total


if __name__ == '__main__':
    # Use relative paths from cwd (must be run from D:\GIT\Tutorial)
    dirs = [
        'dotnet',
        'javascript',
        'architecture',
        'distributed-systems',
        'data',
        'web-services',
        'azure',
        'testing',
        'devops',
    ]
    total = process_directories(dirs)
    print(f'\nTotal headings fixed: {total}')
