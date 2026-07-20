# Guideline & Regulatory Adapter Strategy

Do not force all authorities into one generic scraper.

```text
GuidelineProvider
├── WHOAdapter
├── NICEAdapter
├── SpecialtySocietyAdapter
└── NationalGuidelineAdapter

RegulatoryProvider
├── FDAAdapter
├── EMAAdapter
└── NationalRegulatorAdapter
```

Guideline normalized fields: title, issuing body, jurisdiction, specialty,
publication/update date, version, current/superseded/archived status,
recommendations with source locators, canonical URL, provenance.

Regulatory normalized fields: authority, product/ingredient, indication,
approval status/date, label version date, warnings, safety notices,
canonical URL, provenance.

Hard rule: `published clinical study` MUST NOT become `approved indication`.
