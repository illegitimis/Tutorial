#!/usr/bin/env python3
"""Fix empty image alt text in markdown files."""
import re

# All the image fixes: (file, old_url_fragment, alt_text, unreachable)
# unreachable = True means append ⚠ after the markdown
FIXES = [
    # dotnet/aspnet/web-app-mvc6-efcore-angular.md - all livefilestore = 404
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://uz5qia.by3302.livefilestore.com",
        "![ASP.NET Core middleware pipeline diagram](https://uz5qia.by3302.livefilestore.com",
        True,
    ),
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://vbp4kg.by3302.livefilestore.com",
        "![Static files and web essentials screenshot](https://vbp4kg.by3302.livefilestore.com",
        True,
    ),
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://g7xpqg.by3302.livefilestore.com",
        "![CSS box model diagram](https://g7xpqg.by3302.livefilestore.com",
        True,
    ),
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://hiqm5q.by3302.livefilestore.com",
        "![MVC 6 framework overview](https://hiqm5q.by3302.livefilestore.com",
        True,
    ),
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://jxhreg.by3302.livefilestore.com",
        "![View models screenshot](https://jxhreg.by3302.livefilestore.com",
        True,
    ),
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://wowstq.by3302.livefilestore.com",
        "![Default font icon buttons screenshot](https://wowstq.by3302.livefilestore.com",
        True,
    ),
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://tcywqq.by3302.livefilestore.com",
        "![Bootstrap grid form-group layout](https://tcywqq.by3302.livefilestore.com",
        True,
    ),
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://6ebyoa.by3302.livefilestore.com",
        "![EF Core data model diagram](https://6ebyoa.by3302.livefilestore.com",
        True,
    ),
    (
        "dotnet/aspnet/web-app-mvc6-efcore-angular.md",
        "![](https://hiqk5q.by3302.livefilestore.com",
        "![AngularJS controller code screenshot](https://hiqk5q.by3302.livefilestore.com",
        True,
    ),
    # javascript/angular/fundamentals.md - all livefilestore = 404
    (
        "javascript/angular/fundamentals.md",
        "![](https://wewstq.by3302.livefilestore.com",
        "![Angular directive syntax examples](https://wewstq.by3302.livefilestore.com",
        True,
    ),
    (
        "javascript/angular/fundamentals.md",
        "![](https://tsywqq.by3302.livefilestore.com",
        "![Angular directive attribute form](https://tsywqq.by3302.livefilestore.com",
        True,
    ),
    (
        "javascript/angular/fundamentals.md",
        "![](https://6ubyoa.by3302.livefilestore.com",
        "![Angular directive class form](https://6ubyoa.by3302.livefilestore.com",
        True,
    ),
    (
        "javascript/angular/fundamentals.md",
        "![](https://jnhreg.by3302.livefilestore.com",
        "![Angular event directives reference](https://jnhreg.by3302.livefilestore.com",
        True,
    ),
    (
        "javascript/angular/fundamentals.md",
        "![](https://gonhua.by3302.livefilestore.com",
        "![Angular built-in services overview](https://gonhua.by3302.livefilestore.com",
        True,
    ),
    # architecture/domain-strength.md - lostechies images = 200
    (
        "architecture/domain-strength.md",
        "![](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb1.png)",
        "![Domain model case-centric diagram](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb1.png)",
        False,
    ),
    (
        "architecture/domain-strength.md",
        "![](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb2.png)",
        "![Permission and task model diagram](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb2.png)",
        False,
    ),
    (
        "architecture/domain-strength.md",
        "![](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb3.png)",
        "![Configurable workflow states diagram](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb3.png)",
        False,
    ),
    (
        "architecture/domain-strength.md",
        "![](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb4.png)",
        "![CQRS controller handler code](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb4.png)",
        False,
    ),
    (
        "architecture/domain-strength.md",
        "![](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb5.png)",
        "![Single-action handler code](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb5.png)",
        False,
    ),
    (
        "architecture/domain-strength.md",
        "![](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb6.png)",
        "![Anti-corruption layer integration diagram](https://lostechies.com/content/jimmybogard/uploads/2016/06/image_thumb6.png)",
        False,
    ),
    # distributed-systems/microservices-architecture.md - all livefilestore = 404
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://g7xqqg.by3302.livefilestore.com",
        "![Microservice single-purpose diagram](https://g7xqqg.by3302.livefilestore.com",
        True,
    ),
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://hiqn5q.by3302.livefilestore.com",
        "![High cohesion microservice diagram](https://hiqn5q.by3302.livefilestore.com",
        True,
    ),
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://jxhseg.by3302.livefilestore.com",
        "![Autonomous service contracts diagram](https://jxhseg.by3302.livefilestore.com",
        True,
    ),
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://wowttq.by3302.livefilestore.com",
        "![Semantic versioning microservices diagram](https://wowttq.by3302.livefilestore.com",
        True,
    ),
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://tcytqq.by3302.livefilestore.com",
        "![Business domain centric service diagram](https://tcytqq.by3302.livefilestore.com",
        True,
    ),
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://vbp2kg.by3302.livefilestore.com",
        "![Monolith eCommerce architecture](https://vbp2kg.by3302.livefilestore.com",
        True,
    ),
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://uz5oia.by3302.livefilestore.com",
        "![Microservice eCommerce architecture](https://uz5oia.by3302.livefilestore.com",
        True,
    ),
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://6ebvoa.by3302.livefilestore.com",
        "![Microservices communication technology stack](https://6ebvoa.by3302.livefilestore.com",
        True,
    ),
    (
        "distributed-systems/microservices-architecture.md",
        "![](https://fpneua.by3302.livefilestore.com",
        "![API gateway and service registry diagram](https://fpneua.by3302.livefilestore.com",
        True,
    ),
    # azure/lctrs/hybrid.infra.md - local files exist
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h01.png)",
        "![Hybrid infrastructure slide 1](./pics/l02/h01.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h02.png)",
        "![Hybrid infrastructure slide 2](./pics/l02/h02.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h03.png)",
        "![Hybrid infrastructure slide 3](./pics/l02/h03.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h04.png)",
        "![Hybrid infrastructure slide 4](./pics/l02/h04.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h05.png)",
        "![Hybrid infrastructure slide 5](./pics/l02/h05.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h06.png)",
        "![Hybrid infrastructure slide 6](./pics/l02/h06.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h07.png)",
        "![Hybrid infrastructure slide 7](./pics/l02/h07.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h08.png)",
        "![Hybrid infrastructure slide 8](./pics/l02/h08.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h09.png)",
        "![Hybrid infrastructure slide 9](./pics/l02/h09.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h10.png)",
        "![Hybrid infrastructure slide 10](./pics/l02/h10.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h11.png)",
        "![Hybrid infrastructure slide 11](./pics/l02/h11.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h12.png)",
        "![Hybrid infrastructure slide 12](./pics/l02/h12.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h13.png)",
        "![Hybrid infrastructure slide 13](./pics/l02/h13.png)",
        False,
    ),
    (
        "azure/lctrs/hybrid.infra.md",
        "![](./pics/l02/h14.png)",
        "![Hybrid infrastructure slide 14](./pics/l02/h14.png)",
        False,
    ),
    # azure/learn/428-kc.md - docs.microsoft.com = 200
    (
        "azure/learn/428-kc.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-network-connectivity-azure/media/8-architecture.png)",
        "![Azure payment system network architecture](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-network-connectivity-azure/media/8-architecture.png)",
        False,
    ),
    # azure/learn/48-Knowledge-check.md - docs.microsoft.com = 200
    (
        "azure/learn/48-Knowledge-check.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-network-connectivity-azure/media/8-architecture.png)",
        "![Azure payment system network architecture](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-network-connectivity-azure/media/8-architecture.png)",
        False,
    ),
    # azure/learn/513-aad.md - docs.microsoft.com = 200
    (
        "azure/learn/513-aad.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-access-azure-identity-services/media/3-azure-active-directory.png)",
        "![Azure Active Directory tenant diagram](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-access-azure-identity-services/media/3-azure-active-directory.png)",
        False,
    ),
    (
        "azure/learn/513-aad.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-access-azure-identity-services/media/3-azure-ad-connect.png)",
        "![Azure AD Connect sync diagram](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-access-azure-identity-services/media/3-azure-ad-connect.png)",
        False,
    ),
    # azure/learn/514-mfa-ca.md - docs.microsoft.com = 200
    (
        "azure/learn/514-mfa-ca.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-access-azure-identity-services/media/4-conditional-access-signal-decision-enforcement.png)",
        "![Conditional Access signal decision flow](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-access-azure-identity-services/media/4-conditional-access-signal-decision-enforcement.png)",
        False,
    ),
    # azure/learn/522-rbac.md - docs.microsoft.com = 200
    (
        "azure/learn/522-rbac.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/build-cloud-governance-strategy-azure/media/4-role-scope-0223bfae.png)",
        "![Azure RBAC role and scope diagram](https://docs.microsoft.com/en-us/learn/azure-fundamentals/build-cloud-governance-strategy-azure/media/4-role-scope-0223bfae.png)",
        False,
    ),
    # azure/learn/523-rsrc-locks.md - docs.microsoft.com = 200
    (
        "azure/learn/523-rsrc-locks.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/build-cloud-governance-strategy-azure/media/7-portal-add-lock-ebc3d24c.png)",
        "![Azure portal add resource lock](https://docs.microsoft.com/en-us/learn/azure-fundamentals/build-cloud-governance-strategy-azure/media/7-portal-add-lock-ebc3d24c.png)",
        False,
    ),
    # azure/learn/524-ex-del-protect.md - local file exists
    (
        "azure/learn/524-ex-del-protect.md",
        "![](524-payasyougo.png)",
        "![Pay-as-you-go subscription selection](524-payasyougo.png)",
        False,
    ),
    # azure/learn/617-kc.md - docs.microsoft.com = 200
    (
        "azure/learn/617-kc.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/plan-manage-azure-costs/media/7-dev-test-environments.svg)",
        "![Dev and test environment architecture](https://docs.microsoft.com/en-us/learn/azure-fundamentals/plan-manage-azure-costs/media/7-dev-test-environments.svg)",
        False,
    ),
    # azure/legend.md - docs.microsoft.com = 200
    (
        "azure/legend.md",
        "![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/protect-against-security-threats-azure/media/6-dedicated-hosts-cab8e670.png)",
        "![Azure Dedicated Host physical server diagram](https://docs.microsoft.com/en-us/learn/azure-fundamentals/protect-against-security-threats-azure/media/6-dedicated-hosts-cab8e670.png)",
        False,
    ),
]


def apply_fixes():
    files_changed = {}
    images_fixed = 0
    images_unreachable = 0

    for filepath, old_fragment, new_fragment, unreachable in FIXES:
        if filepath not in files_changed:
            with open(filepath, 'r', encoding='utf-8') as f:
                files_changed[filepath] = f.read()

        content = files_changed[filepath]

        if old_fragment in content:
            replacement = new_fragment
            if unreachable:
                # For livefilestore URLs, we need to handle the full URL line
                # The old_fragment is just the start of the URL, so we need to find the full pattern
                # Find the complete image markdown: ![](URL)
                pattern = re.escape(old_fragment)
                # Match the full image markdown starting with old_fragment
                full_pattern = re.escape("![](") + r'(' + re.escape(old_fragment[4:]) + r'[^)]*\))'
                # Actually just do a simple prefix replacement
                # old_fragment = "![](https://..."
                # We need to find "![](https://...?...)" and replace with new
                # Simpler: find ![](URL) where URL starts with old_fragment[4:]
                url_start = old_fragment[4:]  # remove "![]("
                # find "![](url_start...)" in content
                idx = content.find(old_fragment)
                if idx >= 0:
                    # Find end of this image tag
                    end_idx = content.find(')', idx + len(old_fragment))
                    if end_idx >= 0:
                        old_full = content[idx:end_idx+1]
                        new_full = new_fragment + content[idx + len(old_fragment):end_idx+1] + " ⚠"
                        content = content[:idx] + new_full + content[end_idx+1:]
                        files_changed[filepath] = content
                        images_fixed += 1
                        images_unreachable += 1
                        print(f"  FIXED (404): {filepath} - {new_fragment[:60]}...")
            else:
                # Exact full replacement
                if old_fragment in content:
                    content = content.replace(old_fragment, new_fragment, 1)
                    files_changed[filepath] = content
                    images_fixed += 1
                    print(f"  FIXED (200): {filepath} - {new_fragment[:60]}...")
        else:
            print(f"  NOT FOUND: {filepath} - {old_fragment[:60]}...")

    # Write all changed files
    for filepath, content in files_changed.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Written: {filepath}")

    return images_fixed, images_unreachable


if __name__ == '__main__':
    fixed, unreachable = apply_fixes()
    print(f"\nImages fixed: {fixed}")
    print(f"Images unreachable (⚠): {unreachable}")
