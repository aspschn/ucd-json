import parsers

# UCD files and parser.
ucd_files = {
    'ArabicShaping.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'BidiBrackets.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'BidiCharacterTest.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'BidiMirroring.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'BidiTest.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'Blocks.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },
    'CJKRadicals.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'CaseFolding.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'CompositionExclusions.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'DerivedAge.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },
    'DerivedCoreProperties.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'DerivedNormalizationProps.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'EastAsianWidth.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },
    'EmojiSources.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'EquivalentUnifiedIdeograph.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'HangulSyllableType.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },
    'Index.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'IndicPositionalCategory.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },
    'IndicSyllabicCategory.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'Jamo.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'LineBreak.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'NameAliases.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'NamedSequences.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'NamedSequencesProv.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'NamesList.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'NormalizationCorrections.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'NormalizationTest.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'NushuSources.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'PropList.txt': {
        'parser': parsers.GroupedRangeParser,
        'type': 'ucd',
    },
    'PropertyAliases.txt': {
        'parser': parsers.SimpleKeyValueParser,
        'type': 'ucd',
    },
    'PropertyValueAliases.txt': {
        'parser': parsers.GroupedSimpleKeyValueParser,
        'type': 'ucd',
    },
    'ScriptExtensions.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'Scripts.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },
    'SpecialCasing.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'StandardizedVariants.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'TangutSources.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'USourceData.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'UnicodeData.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'VerticalOrientation.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },

    'auxiliary/GraphemeBreakProperty.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'auxiliary/GraphemeBreakTest.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'auxiliary/LineBreakTest.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'auxiliary/SentenceBreakProperty.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'auxiliary/SentenceBreakTest.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'auxiliary/WordBreakProperty.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'auxiliary/WordBreakTest.txt': {
        'parser': None,
        'type': 'ucd',
    },

    'extracted/DerivedBidiClass.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedBinaryProperties.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedCombiningClass.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedDecompositionType.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedEastAsianWidth.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedGeneralCategory.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },
    'extracted/DerivedJoiningGroup.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedJoiningType.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedLineBreak.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedName.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'ucd',
    },
    'extracted/DerivedNumericType.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'extracted/DerivedNumericValues.txt': {
        'parser': None,
        'type': 'ucd',
    },
    'emoji-data.txt': {
        'parser': parsers.RangeValueParser,
        'type': 'emoji',
    },
    'emoji-sequences.txt': {
        'parser': None,
        'type': 'emoji',
    },
    'emoji-test.txt': {
        'parser': None,
        'type': 'emoji',
    },
    'emoji-variation-sequences.txt': {
        'parser': None,
        'type': 'emoji',
    },
    'emoji-zwj-sequences.txt': {
        'parser': None,
        'type': 'emoji',
    },
}
