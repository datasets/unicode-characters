---
datapackage:
  title: Unicode Codes
  description: The Unicode Consortium is the standards body for the internationalization of software and services. Deployed on more than 20 billion devices around the world, Unicode also provides the solution for internationalization and the architecture to support localization.
  created: 2024-01-01
  updated: 2024-01-31
  licenses:
  - path: http://opendatacommons.org/licenses/pddl/
    title: Open Data Commons Public Domain Dedication and License v1.0
  sources:
  - path: https://home.unicode.org/
    title: Link to data source
  resources:
  - name: unicode-codes
    title: Unicode codes
    description: Unicode codes
    lastModified: 2024-10-10
    path: data.csv
---


The following table describes the format and meaning of each field in a data entry in the UnicodeData. Fields which contain normative information are so indicated.

| Field | Name | Status | Explanation |
| --- | --- | --- | --- |
| 0   | Code value | normative | Code value in 4-digit hexadecimal format. |
| 1   | Character name | normative | These names match exactly the names published in Chapter 7 of the Unicode Standard, Version 2.0, except for the two additional characters. |
| 2   | [General category](ReadMe-3.0.0d3.html#General Category) | normative / informative (see below) | This is a useful breakdown into various "character types" which can be used as a default categorization in implementations. See below for a brief explanation. |
| 3   | [Canonical combining classes](ReadMe-3.0.0d3.html#Canonical Combining Classes) | normative | The classes used for the Canonical Ordering Algorithm in the Unicode Standard. These classes are also printed in Chapter 4 of the Unicode Standard. |
| 4   | [Bidirectional category](ReadMe-3.0.0d3.html#Bidirectional Category) | normative | See the list below for an explanation of the abbreviations used in this field. These are the categories required by the Bidirectional Behavior Algorithm in the Unicode Standard. These categories are summarized in Chapter 3 of the Unicode Standard. |
| 5   | [Character decomposition mapping](ReadMe-3.0.0d3.html#Character Decomposition) | normative | In the Unicode Standard, not all of the mappings are full (maximal) decompositions. Recursive application of look-up for decompositions will, in all cases, lead to a maximal decomposition. The decomposition mappings match exactly the decomposition mappings published with the character names in the Unicode Standard. |
| 6   | Decimal digit value | normative | This is a numeric field. If the character has the decimal digit property, as specified in Chapter 4 of the Unicode Standard, the value of that digit is represented with an integer value in this field |
| 7   | Digit value | normative | This is a numeric field. If the character represents a digit, not necessarily a decimal digit, the value is here. This covers digits which do not form decimal radix forms, such as the compatibility superscript digits |
| 8   | Numeric value | normative | This is a numeric field. If the character has the numeric property, as specified in Chapter 4 of the Unicode Standard, the value of that character is represented with an integer or rational number in this field. This includes fractions as, e.g., "1/5" for U+2155 VULGAR FRACTION ONE FIFTH Also included are numerical values for compatibility characters such as circled numbers. |
| 8   | Mirrored | normative | If the character has been identified as a "mirrored" character in bidirectional text, this field has the value "Y"; otherwise "N". The list of mirrored characters is also printed in Chapter 4 of the Unicode Standard. |
| 10  | Unicode 1.0 Name | informative | This is the old name as published in Unicode 1.0. This name is only provided when it is significantly different from the Unicode 3.0 name for the character. |
| 11  | 10646 comment field | informative | This is the ISO 10646 comment field. It is in parantheses in the 10646 names list. |
| 12  | [Uppercase mapping](ReadMe-3.0.0d3.html#Case Mappings) | informative | Upper case equivalent mapping. If a character is part of an alphabet with case distinctions, and has an upper case equivalent, then the upper case equivalent is in this field. See the explanation below on case distinctions. These mappings are always one-to-one, not one-to-many or many-to-one. This field is informative. |
| 13  | [Lowercase mapping](ReadMe-3.0.0d3.html#Case Mappings) | informative | Similar to [Uppercase mapping](ReadMe-3.0.0d3.html#Case Mappings) |
| 14  | [Titlecase mapping](ReadMe-3.0.0d3.html#Case Mappings) | informative | Similar to [Uppercase mapping](ReadMe-3.0.0d3.html#Case Mappings) |

### General Category

The values in this field are abbreviations for the following. Some of the values are normative, and some are informative. For more information, see the Unicode Standard.

**Note:** the standard does not assign information to control characters (except for certain cases in the Bidirectional Algorithm). Implementations will generally also assign categories to certain control characters, notably CR and LF, according to platform conventions.

#### Normative Categories

| Abbr. | Description |
| --- | --- |
| Lu  | Letter, Uppercase |
| Ll  | Letter, Lowercase |
| Lt  | Letter, Titlecase |
| Mn  | Mark, Non-Spacing |
| Mc  | Mark, Spacing Combining |
| Me  | Mark, Enclosing |
| Nd  | Number, Decimal Digit |
| Nl  | Number, Letter |
| No  | Number, Other |
| Zs  | Separator, Space |
| Zl  | Separator, Line |
| Zp  | Separator, Paragraph |
| Cc  | Other, Control |
| Cf  | Other, Format |
| Cs  | Other, Surrogate |
| Co  | Other, Private Use |
| Cn  | Other, Not Assigned (no characters in the file have this property) |

#### Informative Categories

| Abbr. | Description |
| --- | --- |
| Lm  | Letter, Modifier |
| Lo  | Letter, Other |
| Pc  | Punctuation, Connector |
| Pd  | Punctuation, Dash |
| Ps  | Punctuation, Open |
| Pe  | Punctuation, Close |
| Pi  | Punctuation, Initial quote (may behave like Ps or Pe depending on usage) |
| Pf  | Punctuation, Final quote (may behave like Ps or Pe depending on usage) |
| Po  | Punctuation, Other |
| Sm  | Symbol, Math |
| Sc  | Symbol, Currency |
| Sk  | Symbol, Modifier |
| So  | Symbol, Other |

### Bidirectional Category

Please refer to Chapter 3 for an explanation of the algorithm for Bidirectional Behavior and an explanation of the significance of these categories. An up-to-date version can be found on [Unicode Technical Report #9](http://www.unicode.org/unicode/reports/tr9/). These values are normative.

### Character Decomposition

The decomposition is a normative property of a character. The tags supplied with certain decomposition mappings generally indicate formatting information. Where no such tag is given, the mapping is designated as canonical. Conversely, the presence of a formatting tag also indicates that the mapping is a compatibility mapping and not a canonical mapping. In the absence of other formatting information in a compatibility mapping, the tag is used to distinguish it from canonical mappings.

In some instances a canonical mapping or a compatibility mapping may consist of a single character. For a canonical mapping, this indicates that the character is a canonical equivalent of another single character. For a compatibility mapping, this indicates that the character is a compatibility equivalent of another single character. The compatibility formatting tags used are:

| Tag | Description |
| --- | --- |
| \<font\> | A font variant (e.g. a blackletter form). |
| \<noBreak\> | A no-break version of a space or hyphen. |
| \<initial\> | An initial presentation form (Arabic). |
| \<medial\> | A medial presentation form (Arabic). |
| \<final\> | A final presentation form (Arabic). |
| \<isolated\> | An isolated presentation form (Arabic). |
| \<circle\> | An encircled form. |
| \<super\> | A superscript form. |
| \<sub\> | A subscript form. |
| \<vertical\> | A vertical layout presentation form. |
| \<wide\> | A wide (or zenkaku) compatibility character. |
| \<narrow\> | A narrow (or hankaku) compatibility character. |
| \<small\> | A small variant form (CNS compatibility). |
| \<square\> | A CJK squared font variant. |
| \<fraction\> | A vulgar fraction form. |
| \<compat\> | Otherwise unspecified compatibility character. |

**Reminder:** There is a difference between decomposition and decomposition mapping. The decomposition mappings are defined in the UnicodeData, while the decomposition (also termed "full decomposition") is defined in Chapter 3 to use those mappings recursively.

*   The canonical decomposition is formed by recursively applying the canonical mappings, then applying the canonical reordering algorithm.
*   The compatibility decomposition is formed by recursively applying the canonical _and_ compatibility mappings, then applying the canonical reordering algorithm.

### Canonical Combining Classes

| Value | Description |
| --- | --- |
| 0:  | Spacing, split, enclosing, reordrant, and Tibetan subjoined |
| 1:  | Overlays and interior |
| 7:  | Nuktas |
| 8:  | Hiragana/Katakana voicing marks |
| 9:  | Viramas |
| 10: | Start of fixed position classes |
| 199: | End of fixed position classes |
| 200: | Below left attached |
| 202: | Below attached |
| 204: | Below right attached |
| 208: | Left attached (reordrant around single base character) |
| 210: | Right attached |
| 212: | Above left attached |
| 214: | Above attached |
| 216: | Above right attached |
| 218: | Below left |
| 220: | Below |
| 222: | Below right |
| 224: | Left (reordrant around single base character) |
| 226: | Right |
| 228: | Above left |
| 230: | Above |
| 232: | Above right |
| 233: | Double below |
| 234: | Double above |
| 240: | Below (iota subscript) |

**Note:** some of the combining classes in this list do not currently have members but are specified here for completeness.

### Decompositions and Normalization

Decomposition is specified in Chapter three. The Unicode Technical Report #15 Normalization Forms specifies the interaction between decomposition and normalization. The most up-to-date version is found on [http://www.unicode.org/unicode/reports/tr15/](http://www.unicode.org/unicode/reports/tr15/). That report specifies how the decompositions defined in the Unicode Character Database are used to derive normalized forms of Unicode text.

Note that as of the 2.1.9 update of the Unicode Character Database, the decompositions in the UnicodeData.txt file can be used to recursively derive the full decomposition in canonical order, without the need to separately apply canonical reordering. However, canonical reordering of combining character sequences must still be applied in decomposition when normalizing source text which contains any combining marks.

### Case Mappings

The case mapping is an informative, default mapping. Case itself, on the other hand, has normative status. Thus, for example, 0041 LATIN CAPITAL LETTER A is normatively uppercase, but its lowercase mapping the 0061 LATIN SMALL LETTER A is informative. The reason for this is that case can be considered to be an inherent property of a particular character (and is usually, but not always, derivable from the presence of the terms "CAPITAL" or "SMALL" in the character name), but case mappings between characters are occasionally influenced by local conventions. For example, certain languages, such as Turkish, German, French, or Greek may have small deviations from the default mappings listed in UnicodeData.

In addition to uppercase and lowercase, because of the inclusion of certain composite characters for compatibility, such as 01F1 LATIN CAPITAL LETTER DZ, there is a third case, called _titlecase_, which is used where the first letter of a word is to be capitalized (e.g. UPPERCASE, Titlecase, lowercase). An example of such a titlecase letter is 01F2 LATIN CAPITAL LETTER D WITH SMALL LETTER Z.

The uppercase, titlecase and lowercase fields are only included for characters that have a single corresponding character of that type. Composite characters (such as "339D SQUARE CM") that do not have a single corresponding character of that type can be cased by decomposition.

For compatibility with existing parsers, UnicodeData only contains case mappings for characters where they are one-to-one mappings; it also omits information about context-sensitive case mappings. Information about these special cases can be found in a separate data file, [SpecialCasing.txt](ftp://ftp.unicode.org/Public/UNIDATA/SpecialCasing.txt), which has been added starting with the 2.1.8 update to the Unicode data files. SpecialCasing.txt contains additional informative case mappings that are either not one-to-one or which are context-sensitive.

## Property Invariants

Values in the Unicode Character Database are subject to correction as errors are found; however, some characteristics of the categories themselves can be considered invariants. Applications may wish to take these invariants into account when choosing how to implement character properties. The following is a partial list of known invariants for the Unicode Character Database.

#### Database Fields

*   The number of fields in the Unicode Character Database is fixed.
*   The order of the fields is also fixed.
    *   Any additional information about character properties to be added in the future will appear in separate data tables, rather than being added on to the existing table or by subdivision or reinterpretation of existing fields.

#### General Category

*   There will never be more than 32 General Category values.
    *   It is very unlikely that the Unicode Technical Committee will subdivide the General Category partition any further, since that can cause implementations to misbehave. Because the General Category is limited to 32 values, 5 bits can be used to represent the information, and a 32-bit integer can be used as a bitmask to represent arbitrary sets of categories.

#### Combining Classes

*   Combining classes are limited to the values 0 to 255.
    *   In practice, there are far fewer than 256 values used. Implementations may take advantage of this fact for compression, since only the ordering of the non-zero values matters for the Canonical Reordering Algorithm. It is possible for up to 256 values to be used in the future; however, UTC decisions in the future may restrict the number of values to 128, since this has implementation advantages. \[Signed bytes can be used without widening to ints in Java, for example.\]
*   All characters other than those of General Category M\* have the combining class 0.
    *   Currently, all characters other than those of General Category Mn have the value 0. However, some characters of General Category Me or Mc may be given non-zero values in the future.
    *   The precise values above the value 0 are not invariant--only the relative ordering is considered normative. For example, it is not guaranteed in future versions that the class of U+05B4 will be precisely 14.

#### Case

*   Characters of type Lu, Lt, or Ll are called _cased_. All characters with an Upper, Lower, or Titlecase mapping are cased characters.
    *   However, characters with the General Categories of Lu, Ll, or Lt may not always have case mappings, and case mappings may vary by locale. (See ftp://ftp.unicode.org/Public/UNIDATA/SpecialCasing.txt).

#### Canonical Decomposition

*   Canonical mappings are always in canonical order.
*   Canonical mappings have only the first of a pair possibly further decomposing.
*   Canonical decompositions are "transparent" to other character data:
    *   BIDI(a) = BIDI(principal(canonicalDecomposition(a))
    *   Category(a) = Category(principal(canonicalDecomposition(a))
    *   CombiningClass(a) = CombiningClass(principal(canonicalDecomposition(a))  
        where principal(a) is the first character not of type Mn, or the first character if all characters are of type Mn.
*   However, because there are sometimes missing case pairs, and because of some legacy characters, it is only generally true that:
    *   upper(canonicalDecomposition(a)) = canonicalDecomposition(upper(a))
    *   lower(canonicalDecomposition(a)) = canonicalDecomposition(lower(a))
    *   title(canonicalDecomposition(a)) = canonicalDecomposition(title(a))


Source: https://unicode.org/

