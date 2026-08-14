# X Tag Searcher Migration Checklist

Use this checklist to move the video tag filter out of `TagSearcher`.
Then change `TagSearcher` into the `X Tag Searcher` component.

This checklist exists because the first Tag Searcher design was not clear enough.
In the first version, clicking a tag did not open an X / Twitter search.
Instead, the app treated the clicked tag as a video filter and changed the video results shown in Video Analyze.
Because of that, Tag Searcher behaved like another Video Analyze filter instead of a separate X / Twitter search entry.

This migration separates the two jobs.
Video Analyze keeps the video tag filter.
X Tag Searcher becomes a simple entry point for X / Twitter search.
Do this without breaking the current Video Analyze feature.

## Check Current State

- [ ] Check the current `TagSearcher` props, events, and display content.
- [ ] Check the data and callbacks that `App.tsx` sends to `TagSearcher`.
- [ ] Check how `useVideos` provides `allTags`, `selectedTags`, `toggleTag`, and the filter flow.
- [ ] Check how the video tag filter changes `filteredVideos`.
- [ ] Check if text search, playlist filter, and tag filter can work together.
- [ ] Write down the current Video tag filter steps and expected results. Use them as the baseline after the split.
- [ ] Check if CSS such as `.tag-list` and `.tag-pill` is also used by other sections.
- [ ] Check when X Tag Searcher is shown for each publication version and when it gets the `In progress` label.

## Split Work

- [ ] Create a separate Video tag filter component.
- [ ] Move the video tag buttons and selected state from `TagSearcher` to the Video tag filter component.
- [ ] Connect `allTags`, `selectedTags`, and `toggleTag` back to the Video Analyze section.
- [ ] Make sure the existing tag filter logic in `useVideos` keeps the same behavior after the split.
- [ ] Create a JSON data file only for X Tag Searcher.
- [ ] Define category and tag data based on `tag-searcher-data-design.md`.
- [ ] Change `TagSearcher` to read the separate JSON file.
- [ ] Change `TagSearcher` to show tags by category.
- [ ] Use each tag `query` to create an X / Twitter search URL.
- [ ] Open the search result in a new tab when the tag label is clicked.
- [ ] Make sure the description is not part of the link.
- [ ] Add desktop and mobile styles only for X Tag Searcher.
- [ ] Make sure the new X Tag Searcher styles do not change the Video tag filter look or behavior.

## Check Results

### Video Tag Filter Regression

- [ ] The Video tag filter still shows tags from the current video data.
- [ ] After clicking one video tag, the video results only show matching items.
- [ ] Clicking the selected video tag again removes that filter.
- [ ] The existing behavior for selecting multiple video tags does not change.
- [ ] `Clear` clears video tags, playlist filter, and text search.
- [ ] Video text search still works.
- [ ] Playlist filter still works.
- [ ] Switching between Table and Gallery keeps the current filter results.
- [ ] The shown video count matches the real filter results.

### X Tag Searcher Feature

- [ ] X Tag Searcher uses its own JSON file, not the tag list from `videos.json`.
- [ ] Categories and tags are shown in JSON order.
- [ ] A tag with a description shows that description.
- [ ] No empty description area is shown when the description is empty or missing.
- [ ] Only the tag label is clickable.
- [ ] Clicking a tag label opens a new tab.
- [ ] The search URL uses `https://x.com/search?q=${encodeURIComponent(query)}&src=typed_query`.
- [ ] Japanese, English, spaces, `#`, quotes, and other characters are URL encoded correctly.
- [ ] The search URL does not add `&f=live` or any other sort option.
- [ ] Empty categories are not shown.
- [ ] If all categories have no tags, the whole X Tag Searcher section is not shown.

### Layout And Usability

- [ ] On desktop, categories and tags do not overlap or overflow.
- [ ] On mobile, categories and tags can stack or wrap.
- [ ] On mobile, there is no horizontal scroll.
- [ ] On mobile, the description does not depend on hover.
- [ ] The tag label tap area is large enough for mobile use.
- [ ] The Video tag filter and the X Tag Searcher handoff to X / Twitter are easy to tell apart on screen and in meaning.

### Automatic Checks

- [ ] Run lint and check that there are no errors.
- [ ] Run build and check that there are no type or bundle errors.
- [ ] Finish the final X Tag Searcher acceptance check in `tag-searcher-checklist.md`.
