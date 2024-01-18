ucd-json
=============

ucd-json is a tool for convert various text Unicode UCD data files to JSON format.

UCD data files
----------------
ucd-json downloads it's data from online during usage. If first run or other version requested, network connection should needed.

Files will downloaded under directory `data/{version}/`, `data/emoji/{version}/` which version is Unicode/Emoji version.

Usage
---------------

To list all available files,
```sh
$ ./ucd-json -l
```

then transform file to json by
```sh
$ ./ucd-json PropertyAliases.txt
```

You can also redirect the output to write result as file.
```sh
$ ./ucd-json PropertyValueAliases.txt > PropertyValueAliases.json
```

For @missing convention which is introduced from Unicode 15.0.0,
```sh
$ ./ucd-json --missing extracted/DerivedBidiClass.txt > DerivedBidiClass.missing.json
```

Coverage
---------

### UCD files

| File                           | Status          | Parser                                 |
| ------------------------------ | --------------- | -------------------------------------- |
| ArabicShaping.txt              | Not implemented |                   |
| BidiBrackets.txt               | Not implemented |                   |
| BidiCharacterTest.txt          | Not implemented |                   |
| BidiMirroring.txt              | Not implemented |                   |
| BidiTest.txt                   | Not implemented |                   |
| Blocks.txt                     | Done            | [RangeValueParser](#rangevalueparser)  |
| CaseFolding.txt                | Not implemented |                   |
| CJKRadicals.txt                | Not implemented |                   |
| CompositionExclusions.txt      | Done            | [RangeParser](#rangeparser)            |
| DerivedAge.txt                 | Done            | [RangeValueParser](#rangevalueparser)  |
| DerivedCoreProperties.txt      | Not implemented |                   |
| DerivedNormalizationProps.txt  | Done            | NormalizationPropsParser |
| EastAsianWidth.txt             | Done            | [RangeValueParser](#rangevalueparser)  |
| EmojiSources.txt               | Not implemented |                   |
| EquivalentUnifiedIdeograph.txt | Not implemented |                   |
| HangulSyllableType.txt         | Done            | [RangeValueParser](#rangevalueparser)  |
| Index.txt                      | Not implemented |                   |
| IndicPositionalCategory.txt    | Done            | [RangeValueParser](#rangevalueparser)  |
| IndicSyllabicCategory.txt      | Not implemented |                   |
| Jamo.txt                       | Not implemented |                   |
| LineBreak.txt                  | Not implemented |                   |
| NameAliases.txt                | Not implemented |                   |
| NamedSequencesProv.txt         | Not implemented |                   |
| NamedSequences.txt             | Not implemented |                   |
| NamesList.txt                  | Not implemented |                   |
| NormalizationCorrections.txt   | Not implemented |                   |
| NormalizationTest.txt          | Done            | NormalizationTestParser |
| NushuSources.txt               | Not implemented |                   |
| PropertyAliases.txt            | Done            | SimpleKeyValueParser |
| PropertyValueAliases.txt       | Done            | GroupedSimpleKeyValueParser |
| PropList.txt                   | Done            | GroupedRangeParser |
| ScriptExtensions.txt           | Not implemented |                   |
| Scripts.txt                    | Done            | [RangeValueParser](#rangevalueparser)  |
| SpecialCasing.txt              | Not implemented |                   |
| StandardizedVariants.txt       | Not implemented |                   |
| TangutSources.txt              | Not implemented |                   |
| UnicodeData.txt                | Not implemented |                   |
| USourceData.txt                | Not implemented |                   |
| VerticalOrientation.txt        | Not implemented |                   |

| File                                | Status          | Parser            |
| ----------------------------------- | --------------- | ----------------- |
| auxiliary/GraphemeBreakProperty.txt | Done            | [RangeValueParser](#rangevalueparser)  |
| auxiliary/GraphemeBreakTest.txt     | Done            | GraphemeBreakTestParser |
| auxiliary/LineBreakTest.txt         | Not implemented |                   |
| auxiliary/SentenceBreakProperty.txt | Not implemented |                   |
| auxiliary/SentenceBreakTest.txt     | Not implemented |                   |
| auxiliary/WordBreakProperty.txt     | Done            | [RangeValueParser](#rangevalueparser)  |
| auxiliary/WordBreakTest.txt         | Not implemented |                   |
| extracted/DerivedBidiClass.txt         | Not implemented |                   |
| extracted/DerivedBinaryProperties.txt  | Not implemented |                   |
| extracted/DerivedCombiningClass.txt    | Done            | [RangeValueParser](#rangevalueparser)  |
| extracted/DerivedDecompositionType.txt | Not implemented |                   |
| extracted/DerivedEastAsianWidth.txt    | Not implemented |                   |
| extracted/DerivedGeneralCategory.txt   | Done            | [RangeValueParser](#rangevalueparser)  |
| extracted/DerivedJoiningGroup.txt      | Not implemented |                   |
| extracted/DerivedJoiningType.txt       | Not implemented |                   |
| extracted/DerivedLineBreak.txt         | Not implemented |                   |
| extracted/DerivedName.txt              | Done            | [RangeValueParser](#rangevalueparser)  |
| extracted/DerivedNumericType.txt       | Not implemented |                   |
| extracted/DerivedNumericValues.txt     | Not implemented |                   |

### Emoji files

| File                                   | Status          | Parser            |
| -------------------------------------- | --------------- | ----------------- |
| emoji/emoji-data.txt                   | Done            | GroupedRangeParser |
| emoji/emoji-variation-sequences.txt    | Not implemented |                   |
| emoji-sequences.txt                    | Not implemented |                   |
| emoji-test.txt                         | Not implemented |                   |
| emoji-zwj-sequences.txt                | Not implemented |                   |


### Parsers

#### RangeParser

```json
[
  "0958",
  "0959",
  "095A",
  "095B"
]
```

#### RangeValueParser

```json
{
  "0000..007F": "Basic Latin",
  "0080..00FF": "Latin-1 Supplement",
  "0100..017F": "Latin Extended-A",
  "0180..024F": "Latin Extended-B",
  "0250..02AF": "IPA Extensions"
}
```

Single key for no range.

```json
{
  "0000..001F": "1.1",
  "0020..007E": "1.1",
  "007F..009F": "1.1",
  "00A0..00AC": "1.1",
  "00AD": "1.1",
  "00AE..01F5": "1.1"
}
```


License
---------
ucd-json is available under the MIT license. For details, see the LICENSE file.
