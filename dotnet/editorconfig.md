---
title: EditorConfig
layout: default
nav_order: 9
parent: .NET
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# EditorConfig Reference

Reference and analysis for `.editorconfig` configuration in .NET/C# projects.
Covers four sample configs: `dev`, `azurestackfiji`, `kusto.queries`, and `PTM`.

## Links

- EditorConfig Specification [1] — official spec (v0.15.1)
- EditorConfig.org [2] — home page with editor plugin list
- `roslyn/.editorconfig` [3] — authoritative C# reference config
- `runtime/.editorconfig` [4] — .NET runtime reference config
- C# formatting options [5] — MS Learn
- .NET formatting options [6] — MS Learn
- Code-style rules [7] — IDE0001-IDE0180, MS Learn
- Code-style naming rules [8] — MS Learn
- Rule categories [9] — MS Learn
- `EditorConfig Language Service` [10] — VS extension
- `Code Cleanup On Save` [11] — VS extension

## Commonality and Variance Analysis

### Common Ground

All four sample configs agree on:

- `root = true`
- `indent_style = space`, `indent_size = 4` for C# files
- `dotnet_sort_system_directives_first = true`
- `dotnet_style_predefined_type_for_locals_parameters_members = true`
- `dotnet_style_predefined_type_for_member_access = true`
- `csharp_new_line_before_open_brace = all`
- `csharp_new_line_before_catch/else/finally = true`
- `csharp_indent_block_contents = true`, `csharp_indent_braces = false`, `csharp_indent_switch_labels = true`
- All `csharp_space_*` rules (see [Formatting Rules](#formatting-rules))
- Pattern matching: `csharp_style_pattern_matching_over_as_with_null_check/is_with_cast_check = true`
- `csharp_style_throw_expression = true`
- `csharp_style_prefer_index_operator = true`, `csharp_style_prefer_range_operator = true`

> Severity suffixes (`:suggestion`, `:none`, `:silent`) on otherwise-agreeing values are noise and are
> not listed as variances below.

### Variances

Multi-line compound settings (naming rules) are shown as logical units.
Full snippets appear in [Consolidated Reference](#consolidated-annotated-editorconfig-reference).

| Setting | `dev` | `azurestackfiji` | `kusto.queries` | `PTM` |
| --- | --- | --- | --- | --- |
| `insert_final_newline` | `false` | `true` | `false` | `true` |
| `trim_trailing_whitespace` | - | - | - | `true` |
| `charset` | - | `utf-8-bom` | - | `utf-8-bom` |
| `end_of_line` (`[*.cs]`) | `crlf` | - (`lf` in `[*.sh]`) | `crlf` | `crlf` |
| `this.` qualification (field/property/event) | `false` | `false:refactoring` | `true (all three)` | `false:suggestion` |
| parentheses in binary operators | `always_for_clarity` | `always_for_clarity` | `always_for_clarity` | `never_if_unnecessary` |
| `var` for built-in types | `false` | `true:suggestion` | `false` | `false:none` |
| `var` elsewhere | `false` | `true:suggestion` | `false` | `false:suggestion` |
| expression-bodied methods | `false` | `false:none` | `false` | `true:suggestion` |
| expression-bodied constructors | `false` | `false:none` | `false` | `true:suggestion` |
| `csharp_prefer_braces` | `true` | `true:silent` | `true` | `when_multiline:suggestion` |
| `preserve_single_line_statements` | `true` | `true` | `true` | `false` |
| `new_line_before_members_in_object_initializers` | `true` | `true` | `true` | `false` |
| `using` directive placement | `inside_namespace` | - | `inside_namespace` | `outside_namespace` |
| namespace declaration style | - | - | - | `file_scoped` |
| `file_header_template` | MS copyright (basic) | MS copyright + fileName | MS copyright + fileName | - (commented out) |
| naming: non-private static fields | - | PascalCase (3-line rule) | - | PascalCase (3-line rule) |
| naming: non-private readonly fields | - | PascalCase (3-line rule) | - | PascalCase (3-line rule) |
| naming: static fields | - | `s_`camelCase (3-line rule) | - | `s_`camelCase (3-line rule) |
| naming: instance fields | - | `_`camelCase (3-line rule) | - | `_`camelCase (3-line rule) |
| naming: private readonly fields | - | - | - | `_`camelCase (4-line rule, `!static`) |
| naming: private static readonly fields | - | - | - | PascalCase (4-line rule) |
| diagnostic coverage | 2 rules | ~60+ rules (SA+CA+IDE, with sub-section overrides) | 2 rules | ~100+ rules (SA+CA+IDE+Sonar+MA+xUnit+RS) |
| spell checker | - | - | - | `spelling_*` (VS Spell Checker extension) |

## Consolidated Annotated EditorConfig Reference

Values are from the PTM config (most complete). Deviations from other sample files are noted inline.

### Spell Checker (Optional)

Requires the `VS Spell Checker` [12] extension. The `spelling_*` keys are ignored by all other EditorConfig tooling.

```ini
[*]
spelling_languages = en-us,en-gb,fr-fr,fr-be,nl-nl,nl-be
spelling_exclusion_path = exclusion.dic
spelling_checkable_types = all
spelling_error_severity = suggestion
spelling_use_default_exclusion_dictionary = false
```

- `spelling_languages` — BCP 47 tags for active dictionaries; comma-separated; adjust to your project's target languages
- `spelling_exclusion_path` — path to a project-local exclusion word list
- `spelling_checkable_types` — scope: `identifiers`, `comments`, `strings`, or `all`
- `spelling_error_severity` — `suggestion` is informational; `error` blocks saves
- `spelling_use_default_exclusion_dictionary = false` — opts out of the built-in exclusion list

### Core Options

```ini
root = true

[*]
indent_style = space

[*.{cs,vb}]
indent_size = 4
tab_width = 4
charset = utf-8-bom
end_of_line = crlf
insert_final_newline = true
trim_trailing_whitespace = true
```

- `root = true` — stops EditorConfig from searching parent directories; place at repo root
- `indent_style = space` — unanimous; tabs cause alignment issues in mixed editors
- `indent_size = 4` / `tab_width = 4` — standard for C#; matches Visual Studio default
- `charset = utf-8-bom` — required by some MS tooling; `azurestackfiji` and PTM set this; `dev`/`kusto` do not
- `end_of_line = crlf` — Windows standard; `azurestackfiji` omits this globally
- `insert_final_newline = true` — PTM and `azurestackfiji` prefer `true`; `dev`/`kusto` use `false`
- `trim_trailing_whitespace = true` — PTM only; prevents whitespace noise in diffs

### Organize Usings

```ini
dotnet_sort_system_directives_first = true
dotnet_separate_import_directive_groups = false
```

- `dotnet_sort_system_directives_first = true` — places `System.*` before other namespaces; unanimous
- `dotnet_separate_import_directive_groups = false` — no blank line between using groups; all samples agree

### this. and Me. Qualification

```ini
dotnet_style_qualification_for_field = false:suggestion
dotnet_style_qualification_for_property = false:suggestion
dotnet_style_qualification_for_method = false:suggestion
dotnet_style_qualification_for_event = false:suggestion
```

- `false` keeps code concise; no `this.` unless resolving ambiguity
- **Variance:** `kusto.queries` sets field, property, and event to `true`; method stays `false`; `azurestackfiji` uses `:refactoring` severity on all four (silent suggestion)

### Language Keywords vs BCL Types

```ini
dotnet_style_predefined_type_for_locals_parameters_members = true:suggestion
dotnet_style_predefined_type_for_member_access = true:suggestion
```

- Prefer `int` over `System.Int32`, `string` over `System.String`; unanimous across all samples

### Parentheses Preferences

```ini
dotnet_style_parentheses_in_arithmetic_binary_operators = never_if_unnecessary:suggestion
dotnet_style_parentheses_in_other_binary_operators = never_if_unnecessary:suggestion
dotnet_style_parentheses_in_relational_binary_operators = never_if_unnecessary:suggestion
dotnet_style_parentheses_in_other_operators = never_if_unnecessary:suggestion
```

- `never_if_unnecessary` — omit parentheses when precedence is unambiguous; reduces noise (PTM)
- **Variance:** `dev`, `azurestackfiji`, `kusto.queries` use `always_for_clarity` for arithmetic, relational, and other-binary operators; `dotnet_style_parentheses_in_other_operators` is `never_if_unnecessary` in all configs

### Expression-Level Preferences

```ini
dotnet_style_coalesce_expression = true:suggestion
dotnet_style_collection_initializer = true:suggestion
dotnet_style_explicit_tuple_names = true:warning
dotnet_style_null_propagation = true:suggestion
dotnet_style_object_initializer = true:suggestion
dotnet_style_prefer_auto_properties = true:suggestion
dotnet_style_prefer_compound_assignment = true:warning
dotnet_style_prefer_conditional_expression_over_assignment = true:suggestion
dotnet_style_prefer_conditional_expression_over_return = true:suggestion
dotnet_style_prefer_inferred_anonymous_type_member_names = true:suggestion
dotnet_style_prefer_inferred_tuple_names = true:suggestion
dotnet_style_prefer_is_null_check_over_reference_equality_method = true:suggestion
dotnet_style_prefer_simplified_boolean_expressions = true:suggestion
dotnet_style_prefer_simplified_interpolation = true:suggestion
dotnet_style_prefer_collection_expression = when_types_loosely_match:suggestion
dotnet_style_namespace_match_folder = true:suggestion
dotnet_style_operator_placement_when_wrapping = beginning_of_line
dotnet_style_readonly_field = true:warning
dotnet_code_quality_unused_parameters = all:warning
```

- `coalesce_expression` — prefer `x ?? y` over an explicit null-check assignment
- `explicit_tuple_names` — prefer named elements over `.Item1`, `.Item2`; elevated to `:warning`
- `null_propagation` — prefer `x?.y` over `if (x != null) x.y`
- `prefer_compound_assignment` — prefer `x += 1`; elevated to `:warning`
- `prefer_collection_expression = when_types_loosely_match` — C# 12+; uses `[...]` syntax
- `operator_placement_when_wrapping = beginning_of_line` — `&&`/`||` at start of continuation line
- `readonly_field = true:warning` — fields unchanged after construction should be `readonly`
- `unused_parameters = all:warning` — unused parameters indicate design issues

### var Preferences

```ini
csharp_style_var_for_built_in_types = false:none
csharp_style_var_when_type_is_apparent = true:suggestion
csharp_style_var_elsewhere = false:suggestion
```

- `csharp_style_var_for_built_in_types = false` — use explicit type for `int`, `string`, etc.
- `csharp_style_var_when_type_is_apparent = true` — allow `var` when the RHS makes the type obvious
- `csharp_style_var_elsewhere = false` — explicit type everywhere else
- **Variance:** `azurestackfiji` sets all three to `true:suggestion` (prefer `var` everywhere)

### Expression-Bodied Members

```ini
csharp_style_expression_bodied_accessors = true:suggestion
csharp_style_expression_bodied_constructors = true:suggestion
csharp_style_expression_bodied_indexers = true:suggestion
csharp_style_expression_bodied_lambdas = true:suggestion
csharp_style_expression_bodied_local_functions = true:silent
csharp_style_expression_bodied_methods = true:suggestion
csharp_style_expression_bodied_operators = true:silent
csharp_style_expression_bodied_properties = true:suggestion
```

- `accessors/indexers/properties/lambdas` — unanimous `true` across all samples
- `methods/constructors` — PTM uses `true:suggestion`; other samples use `false` (block body preferred)
- `local_functions/operators` — `true:silent` allows but does not enforce expression bodies

### Pattern Matching and Null-Checking

```ini
csharp_style_pattern_matching_over_as_with_null_check = true:suggestion
csharp_style_pattern_matching_over_is_with_cast_check = true:suggestion
csharp_style_prefer_switch_expression = true:suggestion
csharp_style_prefer_pattern_matching = true:suggestion
csharp_style_prefer_not_pattern = true:suggestion
csharp_style_prefer_extended_property_pattern = true:suggestion
csharp_style_conditional_delegate_call = true:warning
csharp_style_prefer_null_check_over_type_check = true:suggestion
```

- `pattern_matching_over_as_with_null_check` — prefer `x is Foo f` over `var f = x as Foo; if (f != null)`
- `pattern_matching_over_is_with_cast_check` — prefer `x is Foo f` over `if (x is Foo) (Foo)x`
- `prefer_not_pattern` — prefer `x is not null` over `!(x is null)`
- `prefer_extended_property_pattern` — `x is { Foo.Bar: 1 }` (C# 10+)
- `conditional_delegate_call = true:warning` — prefer `handler?.Invoke(args)` over null check + invoke

### Code-Block and Modifier Preferences

```ini
csharp_prefer_braces = when_multiline:suggestion
csharp_style_namespace_declarations = file_scoped:suggestion
csharp_prefer_simple_using_statement = true:suggestion
csharp_prefer_static_local_function = true:suggestion
csharp_prefer_static_anonymous_function = true:suggestion
csharp_prefer_simple_default_expression = true:warning
csharp_style_implicit_object_creation_when_type_is_apparent = true:suggestion
csharp_style_prefer_primary_constructors = true:suggestion
csharp_prefer_system_threading_lock = true:suggestion
csharp_style_prefer_method_group_conversion = true:silent
csharp_style_prefer_top_level_statements = true:silent
csharp_using_directive_placement = outside_namespace:suggestion
csharp_preferred_modifier_order = public,private,protected,internal,file,static,extern,new,virtual,abstract,sealed,override,readonly,unsafe,required,volatile,async:suggestion
```

- `prefer_braces = when_multiline` — braces required only for multi-line bodies (PTM); `dev`/`kusto` use `true` (always)
- `prefer_simple_using_statement` — `using var x = ...;` without an extra block
- `namespace_declarations = file_scoped` — C# 10+; `namespace Foo;` syntax (PTM only)
- `prefer_static_local_function` / `prefer_static_anonymous_function` — lambdas that do not capture state should be `static`
- `prefer_simple_default_expression` — prefer `default` over `default(T)`; elevated to `:warning`
- `implicit_object_creation_when_type_is_apparent` — prefer `new()` on the RHS
- `prefer_primary_constructors` — C# 12+; `class Foo(int x)` syntax
- `prefer_system_threading_lock` — C# 13+; `System.Threading.Lock` over `lock(object)`
- `using_directive_placement = outside_namespace` — PTM; `dev`/`kusto` use `inside_namespace`
- `preferred_modifier_order` — includes `file` and `required` (C# 11+); older samples omit these

### Formatting Rules

#### New line preferences

```ini
csharp_new_line_before_open_brace = all
csharp_new_line_before_else = true
csharp_new_line_before_catch = true
csharp_new_line_before_finally = true
csharp_new_line_before_members_in_anonymous_types = false
csharp_new_line_before_members_in_object_initializers = false
csharp_new_line_between_query_expression_clauses = true
```

- `new_line_before_open_brace = all` — **Allman** brace style; unanimous
- `new_line_before_members_in_object_initializers = false` — PTM compact initializers; other samples use `true`

#### Indentation preferences

```ini
csharp_indent_case_contents = true
csharp_indent_case_contents_when_block = true
csharp_indent_switch_labels = true
csharp_indent_labels = one_less_than_current
csharp_indent_block_contents = true
csharp_indent_braces = false
```

- `indent_case_contents = true` — indent code inside `case` blocks
- `indent_switch_labels = true` — indent `case` labels within `switch`
- `indent_labels = one_less_than_current` — goto labels one level less than surrounding code; `azurestackfiji` uses `flush_left`

#### Space preferences

All four samples agree on all spacing rules:

```ini
csharp_space_after_cast = false
csharp_space_after_colon_in_inheritance_clause = true
csharp_space_after_comma = true
csharp_space_after_dot = false
csharp_space_after_keywords_in_control_flow_statements = true
csharp_space_after_semicolon_in_for_statement = true
csharp_space_around_binary_operators = before_and_after
csharp_space_around_declaration_statements = false
csharp_space_before_colon_in_inheritance_clause = true
csharp_space_before_comma = false
csharp_space_before_dot = false
csharp_space_before_open_square_brackets = false
csharp_space_before_semicolon_in_for_statement = false
csharp_space_between_empty_square_brackets = false
csharp_space_between_method_call_empty_parameter_list_parentheses = false
csharp_space_between_method_call_name_and_opening_parenthesis = false
csharp_space_between_method_call_parameter_list_parentheses = false
csharp_space_between_method_declaration_empty_parameter_list_parentheses = false
csharp_space_between_method_declaration_name_and_open_parenthesis = false
csharp_space_between_method_declaration_parameter_list_parentheses = false
csharp_space_between_parentheses = false
csharp_space_between_square_brackets = false
csharp_space_between_attribute_brackets_and_parameters = false
```

- `space_after_cast = false` — `(int)x` not `(int) x`
- `space_after_keywords_in_control_flow_statements = true` — `if (` not `if(`
- `space_around_binary_operators = before_and_after` — `a + b` not `a+b`

#### Wrapping and whitespace

```ini
csharp_preserve_single_line_blocks = true
csharp_preserve_single_line_statements = false
dotnet_style_allow_multiple_blank_lines_experimental = false:silent
dotnet_style_allow_statement_immediately_after_block_experimental = true:silent
```

- `preserve_single_line_blocks = true` — allows `{ }` on one line for auto-properties
- `preserve_single_line_statements = false` — PTM; forces `if (x) return;` onto two lines; other samples use `true`
- `allow_multiple_blank_lines = false` — PTM and `azurestackfiji` enforce this; `dev`/`kusto` allow it

### Naming Styles

Each naming rule requires three correlated entries: a `dotnet_naming_rule.*` (binds symbols to a
style), a `dotnet_naming_symbols.*` (defines the symbol group), and a `dotnet_naming_style.*` (the
naming convention). Rules are evaluated top-to-bottom; first match wins.

#### Interfaces — `I` prefix + PascalCase

```ini
dotnet_naming_rule.interface_should_be_begins_with_i.severity = suggestion
dotnet_naming_rule.interface_should_be_begins_with_i.symbols = interface
dotnet_naming_rule.interface_should_be_begins_with_i.style = begins_with_i

dotnet_naming_symbols.interface.applicable_kinds = interface
dotnet_naming_symbols.interface.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected

dotnet_naming_style.begins_with_i.required_prefix = I
dotnet_naming_style.begins_with_i.capitalization = pascal_case
```

- All interfaces named `IFoo`; unanimous across all samples

#### Types — PascalCase

```ini
dotnet_naming_rule.types_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.types_should_be_pascal_case.symbols = types
dotnet_naming_rule.types_should_be_pascal_case.style = pascal_case

dotnet_naming_symbols.types.applicable_kinds = class, struct, interface, enum
dotnet_naming_symbols.types.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected

dotnet_naming_style.pascal_case.capitalization = pascal_case
```

- `class`, `struct`, `enum`, and `interface` are PascalCase; `interface` appears in `applicable_kinds` as a catch-all — the Interfaces rule above takes priority via first-match semantics

#### Non-field members — PascalCase

```ini
dotnet_naming_rule.non_field_members_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.non_field_members_should_be_pascal_case.symbols = non_field_members
dotnet_naming_rule.non_field_members_should_be_pascal_case.style = pascal_case

dotnet_naming_symbols.non_field_members.applicable_kinds = property, event, method
dotnet_naming_symbols.non_field_members.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
```

- Properties, events, and methods are PascalCase; unanimous

#### Non-private static fields — PascalCase

```ini
dotnet_naming_rule.non_private_static_fields_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.non_private_static_fields_should_be_pascal_case.symbols = non_private_static_fields
dotnet_naming_rule.non_private_static_fields_should_be_pascal_case.style = non_private_static_field_style

dotnet_naming_symbols.non_private_static_fields.applicable_kinds = field
dotnet_naming_symbols.non_private_static_fields.applicable_accessibilities = public, protected, internal, protected_internal, private_protected
dotnet_naming_symbols.non_private_static_fields.required_modifiers = static

dotnet_naming_style.non_private_static_field_style.capitalization = pascal_case
```

- `azurestackfiji` and PTM include this rule; `dev`/`kusto` do not

#### Non-private readonly fields — PascalCase

```ini
dotnet_naming_rule.non_private_readonly_fields_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.non_private_readonly_fields_should_be_pascal_case.symbols = non_private_readonly_fields
dotnet_naming_rule.non_private_readonly_fields_should_be_pascal_case.style = non_private_readonly_field_style

dotnet_naming_symbols.non_private_readonly_fields.applicable_kinds = field
dotnet_naming_symbols.non_private_readonly_fields.applicable_accessibilities = public, protected, internal, protected_internal, private_protected
dotnet_naming_symbols.non_private_readonly_fields.required_modifiers = readonly

dotnet_naming_style.non_private_readonly_field_style.capitalization = pascal_case
```

- `azurestackfiji` and PTM include this rule; covers public/protected `readonly` fields such as `public static readonly string DefaultPath`

#### Static fields — `s_` prefix + camelCase

```ini
dotnet_naming_rule.static_fields_should_be_camel_case.severity = suggestion
dotnet_naming_rule.static_fields_should_be_camel_case.symbols = static_fields
dotnet_naming_rule.static_fields_should_be_camel_case.style = static_field_style

dotnet_naming_symbols.static_fields.applicable_kinds = field
dotnet_naming_symbols.static_fields.applicable_accessibilities = private, internal, private_protected
dotnet_naming_symbols.static_fields.required_modifiers = static

dotnet_naming_style.static_field_style.capitalization = camel_case
dotnet_naming_style.static_field_style.required_prefix = s_
```

- `s_configValue` — `azurestackfiji` and PTM agree on this convention

#### Instance fields — `_` prefix + camelCase

```ini
dotnet_naming_rule.instance_fields_should_be_camel_case.severity = suggestion
dotnet_naming_rule.instance_fields_should_be_camel_case.symbols = instance_fields
dotnet_naming_rule.instance_fields_should_be_camel_case.style = instance_field_style

dotnet_naming_symbols.instance_fields.applicable_kinds = field

dotnet_naming_style.instance_field_style.capitalization = camel_case
dotnet_naming_style.instance_field_style.required_prefix = _
```

- `_myField` — `azurestackfiji` and PTM agree; `dev`/`kusto` do not define this rule

#### Private readonly fields — `_` prefix + camelCase (non-static only)

```ini
dotnet_naming_rule.private_readonly_fields_should_be_underscore_camel_case.severity = warning
dotnet_naming_rule.private_readonly_fields_should_be_underscore_camel_case.symbols = private_readonly_fields
dotnet_naming_rule.private_readonly_fields_should_be_underscore_camel_case.style = private_readonly_field_style

dotnet_naming_symbols.private_readonly_fields.applicable_kinds = field
dotnet_naming_symbols.private_readonly_fields.applicable_accessibilities = private
dotnet_naming_symbols.private_readonly_fields.required_modifiers = readonly
dotnet_naming_symbols.private_readonly_fields.required_modifiers = !static

dotnet_naming_style.private_readonly_field_style.required_prefix = _
dotnet_naming_style.private_readonly_field_style.capitalization = camel_case
```

- PTM only; elevated to `:warning`
- `required_modifiers = !static` explicitly excludes `static readonly` fields from this rule
- `private readonly string _maxRetryCount` — correct; `configurationValue` or `ConfigurationValue` — incorrect

#### Private static readonly fields — PascalCase

```ini
dotnet_naming_rule.private_static_readonly_fields_should_be_pascal_case.severity = warning
dotnet_naming_rule.private_static_readonly_fields_should_be_pascal_case.symbols = private_static_readonly_fields
dotnet_naming_rule.private_static_readonly_fields_should_be_pascal_case.style = private_static_readonly_field_style

dotnet_naming_symbols.private_static_readonly_fields.applicable_kinds = field
dotnet_naming_symbols.private_static_readonly_fields.applicable_accessibilities = private
dotnet_naming_symbols.private_static_readonly_fields.required_modifiers = static, readonly

dotnet_naming_style.private_static_readonly_field_style.capitalization = pascal_case
```

- PTM only; elevated to `:warning`
- Distinguishes from mutable static fields (which use `s_` prefix); read-only statics treated like constants
- `private static readonly string MyConfigurationValue` — correct; `_myConfigurationValue` — incorrect

#### Constants — PascalCase

```ini
dotnet_naming_rule.constants_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.constants_should_be_pascal_case.symbols = constants
dotnet_naming_rule.constants_should_be_pascal_case.style = pascal_case

dotnet_naming_symbols.constants.applicable_kinds = field, local
dotnet_naming_symbols.constants.required_modifiers = const
```

- `azurestackfiji` and PTM both define this rule

#### Locals and parameters — camelCase

```ini
dotnet_naming_rule.locals_should_be_camel_case.severity = suggestion
dotnet_naming_rule.locals_should_be_camel_case.symbols = locals_and_parameters
dotnet_naming_rule.locals_should_be_camel_case.style = camel_case_style

dotnet_naming_symbols.locals_and_parameters.applicable_kinds = parameter, local

dotnet_naming_style.camel_case_style.capitalization = camel_case
```

- All local variables and method parameters use camelCase; `azurestackfiji` and PTM define this rule

#### Local functions — PascalCase

```ini
dotnet_naming_rule.local_functions_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.local_functions_should_be_pascal_case.symbols = local_functions
dotnet_naming_rule.local_functions_should_be_pascal_case.style = local_function_style

dotnet_naming_symbols.local_functions.applicable_kinds = local_function

dotnet_naming_style.local_function_style.capitalization = pascal_case
```

- Local functions use PascalCase — consistent with regular method naming; `azurestackfiji` and PTM define this rule

### Diagnostic Severities

Setting severity in `.editorconfig` overrides the analyzer default.
Valid severities: `none` (disabled), `silent` (hidden), `suggestion`, `warning`, `error`.

#### Built-in IDE analyzers (no additional package required)

```ini
dotnet_diagnostic.IDE0005.severity = warning    # Remove unnecessary using directives
dotnet_diagnostic.IDE0007.severity = suggestion  # Use var
dotnet_diagnostic.IDE0008.severity = suggestion  # Use explicit type
dotnet_diagnostic.IDE0011.severity = suggestion  # Add braces (see csharp_prefer_braces)
dotnet_diagnostic.IDE0020.severity = suggestion  # Use pattern matching to avoid is-check followed by cast
dotnet_diagnostic.IDE0021.severity = suggestion  # Expression body for constructors
dotnet_diagnostic.IDE0022.severity = suggestion  # Expression body for methods
dotnet_diagnostic.IDE0023.severity = silent      # Expression body for operators
dotnet_diagnostic.IDE0024.severity = silent      # Expression body for conversion operators
dotnet_diagnostic.IDE0025.severity = suggestion  # Expression body for properties
dotnet_diagnostic.IDE0026.severity = suggestion  # Expression body for indexers
dotnet_diagnostic.IDE0027.severity = suggestion  # Expression body for accessors
dotnet_diagnostic.IDE0029.severity = suggestion  # Use coalesce expression (nullable)
dotnet_diagnostic.IDE0030.severity = suggestion  # Use coalesce expression
dotnet_diagnostic.IDE0031.severity = suggestion  # Use null propagation
dotnet_diagnostic.IDE0035.severity = suggestion  # Remove unreachable code
dotnet_diagnostic.IDE0036.severity = suggestion  # Order modifiers
dotnet_diagnostic.IDE0038.severity = suggestion  # Use pattern matching to avoid is-check followed by null check
dotnet_diagnostic.IDE0040.severity = suggestion  # Add accessibility modifiers
dotnet_diagnostic.IDE0043.severity = suggestion  # Invalid placeholder in format string
dotnet_diagnostic.IDE0044.severity = warning     # Make field readonly
dotnet_diagnostic.IDE0046.severity = none        # Convert to conditional expression
dotnet_diagnostic.IDE0051.severity = suggestion  # Remove unused private member
dotnet_diagnostic.IDE0052.severity = warning     # Remove unread private member
dotnet_diagnostic.IDE0055.severity = suggestion  # Fix formatting
dotnet_diagnostic.IDE0059.severity = suggestion  # Unnecessary assignment
dotnet_diagnostic.IDE0060.severity = warning     # Remove unused parameter
dotnet_diagnostic.IDE0062.severity = suggestion  # Make local function static
dotnet_diagnostic.IDE0090.severity = suggestion  # Use new(...)
dotnet_diagnostic.IDE1006.severity = warning     # Naming rule violation
dotnet_diagnostic.IDE0160.severity = suggestion  # Use block-scoped namespace
dotnet_diagnostic.IDE0161.severity = suggestion  # Use file-scoped namespace
dotnet_diagnostic.IDE2000.severity = suggestion  # Multiple blank lines
dotnet_diagnostic.IDE2001.severity = warning     # Embedded statement on same line
dotnet_diagnostic.IDE2002.severity = warning     # Blank lines between braces
dotnet_diagnostic.IDE2004.severity = warning     # Blank line after colon in ctor initializer
dotnet_diagnostic.IDE2005.severity = warning     # Blank line after token in conditional expression
dotnet_diagnostic.IDE2006.severity = warning     # Blank line after token in arrow expression
```

- IDE0044: elevated to `warning` — fields unchanged after construction should be `readonly`
- IDE0052: elevated to `warning` — unread private members are dead code
- IDE0060: elevated to `warning` — unused parameters indicate design issues
- IDE1006: elevated to `warning` — naming violations
- IDE2001-IDE2006: whitespace experimental rules; most elevated to `warning` in PTM

#### StyleCop.Analyzers (requires `StyleCop.Analyzers` NuGet package)

```ini
dotnet_diagnostic.SA0001.severity = none   # XML comment analysis disabled
dotnet_diagnostic.SA1101.severity = none   # Prefix local calls with this
dotnet_diagnostic.SA1309.severity = none   # Field names should not begin with _
dotnet_diagnostic.SA1413.severity = none   # Use trailing comma in multi-line initializers
dotnet_diagnostic.SA1600.severity = none   # Elements should be documented
dotnet_diagnostic.SA1633.severity = none   # File should have header
dotnet_diagnostic.SA1649.severity = none   # File name should match first type name
```

- SA1101 and SA1309 are disabled because they conflict with the `this.=false` and `_field` conventions
- SA1413 is disabled — PTM style does not require trailing commas in multi-line initializers

#### .NET CodeAnalyzers (enabled via `EnableNETAnalyzers`)

```ini
# Errors
dotnet_diagnostic.CA1051.severity = error   # Do not declare visible instance fields
dotnet_diagnostic.CA1856.severity = error   # Incorrect usage of ConstantExpected attribute

# Warnings
dotnet_diagnostic.CA1012.severity = warning  # Abstract types should not have public constructors
dotnet_diagnostic.CA1309.severity = warning  # Use ordinal string comparison
dotnet_diagnostic.CA1310.severity = warning  # Specify StringComparison for correctness
dotnet_diagnostic.CA1822.severity = warning  # Make member static
dotnet_diagnostic.CA1860.severity = warning  # Avoid Enumerable.Any()

# Suggestions
dotnet_diagnostic.CA1018.severity = suggestion
dotnet_diagnostic.CA1047.severity = suggestion
dotnet_diagnostic.CA1305.severity = suggestion
dotnet_diagnostic.CA1507.severity = suggestion
dotnet_diagnostic.CA1510.severity = suggestion
dotnet_diagnostic.CA1511.severity = suggestion
dotnet_diagnostic.CA1512.severity = suggestion
dotnet_diagnostic.CA1513.severity = suggestion
dotnet_diagnostic.CA1725.severity = suggestion
dotnet_diagnostic.CA1802.severity = suggestion
dotnet_diagnostic.CA1805.severity = suggestion
dotnet_diagnostic.CA1810.severity = suggestion
dotnet_diagnostic.CA1821.severity = suggestion
dotnet_diagnostic.CA1823.severity = suggestion
dotnet_diagnostic.CA1825.severity = suggestion
dotnet_diagnostic.CA1826.severity = suggestion
dotnet_diagnostic.CA1827.severity = suggestion
dotnet_diagnostic.CA1828.severity = suggestion
dotnet_diagnostic.CA1829.severity = suggestion
dotnet_diagnostic.CA1830.severity = suggestion
dotnet_diagnostic.CA1831.severity = suggestion
dotnet_diagnostic.CA1832.severity = suggestion
dotnet_diagnostic.CA1833.severity = suggestion
dotnet_diagnostic.CA1834.severity = suggestion
dotnet_diagnostic.CA1835.severity = suggestion
dotnet_diagnostic.CA1836.severity = suggestion
dotnet_diagnostic.CA1837.severity = suggestion
dotnet_diagnostic.CA1838.severity = suggestion
dotnet_diagnostic.CA1839.severity = suggestion
dotnet_diagnostic.CA1840.severity = suggestion
dotnet_diagnostic.CA1841.severity = suggestion
dotnet_diagnostic.CA1842.severity = suggestion
dotnet_diagnostic.CA1843.severity = suggestion
dotnet_diagnostic.CA1844.severity = suggestion
dotnet_diagnostic.CA1845.severity = suggestion
dotnet_diagnostic.CA1846.severity = suggestion
dotnet_diagnostic.CA1847.severity = suggestion
dotnet_diagnostic.CA1852.severity = suggestion
dotnet_diagnostic.CA1854.severity = suggestion
dotnet_diagnostic.CA1855.severity = suggestion
dotnet_diagnostic.CA1857.severity = suggestion
dotnet_diagnostic.CA1858.severity = suggestion
dotnet_diagnostic.CA2008.severity = suggestion
dotnet_diagnostic.CA2009.severity = suggestion
dotnet_diagnostic.CA2011.severity = suggestion
dotnet_diagnostic.CA2012.severity = suggestion
dotnet_diagnostic.CA2013.severity = suggestion
dotnet_diagnostic.CA2014.severity = suggestion
dotnet_diagnostic.CA2016.severity = suggestion
dotnet_diagnostic.CA2200.severity = suggestion
dotnet_diagnostic.CA2201.severity = suggestion
dotnet_diagnostic.CA2208.severity = suggestion
dotnet_diagnostic.CA2245.severity = suggestion
dotnet_diagnostic.CA2246.severity = suggestion
dotnet_diagnostic.CA2249.severity = suggestion

# Disabled
dotnet_diagnostic.CA1000.severity = none   # Do not declare static members on generic types
dotnet_diagnostic.CA1001.severity = none   # Types owning disposable fields should implement IDisposable
dotnet_diagnostic.CA1014.severity = none   # Mark assemblies with CLSCompliantAttribute
dotnet_diagnostic.CA1030.severity = none   # Use events where appropriate
dotnet_diagnostic.CA1031.severity = none   # Do not catch general exception types
dotnet_diagnostic.CA1040.severity = none   # Avoid empty interfaces
dotnet_diagnostic.CA1062.severity = none   # Validate arguments of public methods
dotnet_diagnostic.CA1707.severity = silent # Identifiers should not contain underscores
dotnet_diagnostic.CA1711.severity = none   # Identifiers should not have incorrect suffix
dotnet_diagnostic.CA1716.severity = none   # Identifiers should not match keywords
dotnet_diagnostic.CA1724.severity = none   # Type names should not match namespaces
dotnet_diagnostic.CA1812.severity = none   # Avoid uninstantiated internal classes
dotnet_diagnostic.CA1819.severity = none   # Properties should not return arrays
dotnet_diagnostic.CA1848.severity = none   # Use LoggerMessage delegates
dotnet_diagnostic.CA2007.severity = none   # Consider calling ConfigureAwait
dotnet_diagnostic.CA2225.severity = none   # Operator overloads have named alternates
dotnet_diagnostic.CA2326.severity = none   # Do not use TypeNameHandling other than None
dotnet_diagnostic.CA2327.severity = none   # Do not use insecure JsonSerializerSettings
```

- CA1051 elevated to `error` — visible instance fields break encapsulation
- CA1707 set to `silent` — the `_field` convention uses underscores; suppresses false positives
- CA1309/CA1310 elevated to `warning` — string comparison bugs are hard to find at runtime

#### SonarAnalyzer.CSharp (requires `SonarAnalyzer.CSharp` NuGet package)

```ini
dotnet_diagnostic.S112.severity = warning   # Do not throw NullReferenceException
dotnet_diagnostic.S2166.severity = warning  # Class named with 'Exception' suffix should extend Exception
dotnet_diagnostic.S3925.severity = warning  # ISerializable implementation pattern
```

#### Meziantou.Analyzer (requires `Meziantou.Analyzer` NuGet package)

```ini
dotnet_diagnostic.MA0012.severity = warning    # NullReferenceException is a reserved exception type
dotnet_diagnostic.MA0015.severity = warning    # Use ArgumentException overload with parameter name
dotnet_diagnostic.MA0037.severity = error      # Remove empty statement
dotnet_diagnostic.MA0039.severity = warning    # Do not write custom certificate validation
dotnet_diagnostic.MA0049.severity = suggestion # Type name should not match containing namespace
```

#### xunit.analyzers (requires `xunit.analyzers` NuGet package)

```ini
dotnet_diagnostic.xUnit1012.severity = none
dotnet_diagnostic.xUnit1030.severity = none
dotnet_diagnostic.xUnit1031.severity = none
dotnet_diagnostic.xUnit2005.severity = none
dotnet_diagnostic.xUnit2020.severity = none
dotnet_diagnostic.xUnit2023.severity = none
dotnet_diagnostic.xUnit2029.severity = none
```

#### ReSharper / Rider (JetBrains-proprietary)

`resharper_*` keys are honoured only by `Rider` and the `ReSharper` VS extension.
They are silently ignored by `dotnet format`, the `EditorConfig Language Service`, and all other
standard tooling.

```ini
resharper_string_literal_typo_highlighting = hint
resharper_arrange_type_member_modifiers_highlighting = hint
resharper_remove_redundant_braces_highlighting = hint
resharper_suggest_var_or_type_built_in_types_highlighting = none
resharper_member_hides_static_from_outer_class_highlighting = none
resharper_unused_auto_property_accessor_local_highlighting = hint
resharper_unused_member_global_highlighting = hint
```

## Analyzer Enablement

Analyzer settings split into two layers: `.editorconfig` controls per-rule severity; `MSBuild`
properties control which analyzers are loaded at all. Set `MSBuild` properties in
`Directory.Build.props` for repo-wide effect, or directly in a `.csproj` for per-project control.

### Directory.Build.props or .csproj

```xml
<PropertyGroup>
  <EnableNETAnalyzers>true</EnableNETAnalyzers>
  <AnalysisMode>AllEnabledByDefault</AnalysisMode>
  <AnalysisLevel>latest</AnalysisLevel>
</PropertyGroup>
```

- `EnableNETAnalyzers = true` — activates built-in .NET code-quality analyzers (CA rules); required
  for `CA*` diagnostics to fire; available from .NET 5 SDK onwards
- `AnalysisMode` — which rules are active:
  - `Default` — only rules enabled by default (conservative)
  - `AllEnabledByDefault` — enables all rules that are on by default; more comprehensive than `Default`
  - `Minimum` / `Recommended` — progressively more rules
- `AnalysisLevel` — analyzer rule version; `latest` tracks the current SDK;
  pin to e.g. `8.0` to prevent rule changes across SDK upgrades

### Placement

| Location | Scope | Use when |
| --- | --- | --- |
| `Directory.Build.props` (repo root) | All projects in repo | Consistent baseline across the solution |
| `<Project>.csproj` `<PropertyGroup>` | Single project | One project needs a different analysis mode |

When both are set, the `.csproj` value wins (`MSBuild` property override semantics).

## NuGet Configuration

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <config>
    <add key="repositoryPath" value="./packages" />
  </config>
  <packageSources>
    <clear />
    <add key="PrivateFeed" value="https://<org>.pkgs.visualstudio.com/<collection>/_packaging/<feed>/nuget/v3/index.json" />
    <add key="NuGetV3" value="https://api.nuget.org/v3/index.json" />
  </packageSources>
</configuration>
```

- `repositoryPath = ./packages` — stores packages relative to this config file rather than in the global cache
- `<clear />` — removes all inherited sources (user-level and machine-level); ensures only
  explicitly listed feeds are active; critical in enterprise environments
- Private feed — replace `<org>`, `<collection>`, `<feed>` with your Azure DevOps organisation and
  feed names; supports `NuGet` v3 index format
- `NuGetV3` — public `nuget.org` feed; omit in fully air-gapped environments

### nuget.config Hierarchy

`NuGet` merges config files from the solution directory up to user/machine level. A `<clear />` in a
solution-level `nuget.config` prevents inheritance from parent configs.

## File-Type Settings

```ini
[*.json]
indent_size = 2

[*.{csproj,vbproj,vcxproj,vcxproj.filters,proj,projitems,shproj}]
indent_size = 2

[*.{props,targets}]
indent_size = 2

[*.{xml,ruleset,config,nuspec,resx,tasks,vsixmanifest,vsct}]
indent_size = 4

[*.{ps1,psm1}]
indent_size = 4

[*.sh]
end_of_line = lf
indent_size = 2
```

- JSON and `MSBuild` project/config files use 2-space indent — common convention
- General XML files use 4-space indent
- PowerShell scripts use 4-space indent — consistent with PSScriptAnalyzer community convention
- Shell scripts use LF line endings regardless of the global `end_of_line` setting

[1]: https://spec.editorconfig.org/
[2]: https://editorconfig.org/
[3]: https://github.com/dotnet/roslyn/blob/main/.editorconfig
[4]: https://github.com/dotnet/runtime/blob/main/.editorconfig
[5]: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/csharp-formatting-options
[6]: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/dotnet-formatting-options
[7]: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/
[8]: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/naming-rules
[9]: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/categories
[10]: https://marketplace.visualstudio.com/items?itemName=MadsKristensen.EditorConfig
[11]: https://marketplace.visualstudio.com/items?itemName=MadsKristensen.CodeCleanupOnSave
[12]: https://marketplace.visualstudio.com/items?itemName=MadsKristensen.VSSpellChecker

[<](./index.md) | [<<](/index.md)
