# Tag Searcher Data Design

This document defines the JSON data shape used by the Tag Searcher block.

## Data Source

Tag Searcher uses an independent JSON file as its data source.

The JSON top level is `categories`. Each category represents a group of tag search entries and defines the meaning of that group.

The current category model uses two categories: official and unofficial.

- Official: tags actually used or announced by the talent or the operator.
- Unofficial: tags naturally formed by fans, used for fanart, or used for archive organization.

Official and unofficial are temporary categories. They can be replaced with custom categories in the future, so the UI should render categories from the JSON generically.

## JSON Shape

```json
{
  "categories": [
    {
      "id": "official",
      "label": "official",
      "description": "Actually used or announced by the talent.",
      "tags": [
        {
          "id": "official-main",
          "label": "#結萌ひまり",
          "query": "#結萌ひまり",
          "description": ""
        },
        {
          "id": "fanart",
          "label": "#ひまり色",
          "query": "#ひまり色",
          "description": "fanart"
        }
      ]
    },
    {
      "id": "unofficial",
      "label": "unofficial",
      "description": "Formed by fans, used for fanart, or used for archive organization.",
      "tags": [
        {
          "id": "lifestyle",
          "label": "#むすびめから始まる物語",
          "query": "#むすびめから始まる物語",
          "description": "Lifestyle habits started because of むすびめ."
        }
      ]
    }
  ]
}
```

## Category Fields

| Field | Required | Purpose |
| --- | --- | --- |
| `id` | Yes | Stable category identifier. |
| `label` | Yes | Category display name. |
| `description` | No | Optional category meaning and classification rule. |
| `tags` | Yes | Tag entries in this category. |

## Tag Fields

| Field | Required | Purpose |
| --- | --- | --- |
| `id` | Yes | Stable tag identifier. |
| `label` | Yes | Display text shown to users. |
| `query` | Yes | Text used to generate the X/Twitter search URL. |
| `description` | No | Optional explanation shown below the tag label. |

`label` and `query` may be different. For example, the label can be `結萌ひまり` while the query is `"結萌ひまり"`.

The initial version supports one query per tag. It does not support multiple queries or OR-combined query strings.

## Empty Data Rules

- If `description` is empty or missing, do not show description text.
- If a category has no tags, do not show that category.
- If the JSON has no visible tags at all, do not show the Tag Searcher block.
- If the JSON syntax is invalid, treat it as a build or development error rather than a runtime UI state.

## Implementation Mapping

| Design Item | Location |
| --- | --- |
| Tag Searcher component | `src/components/TagSearcher/` |
| Tag data JSON | `src/data/` |
