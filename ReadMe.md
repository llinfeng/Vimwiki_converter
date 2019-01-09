
This scripts converts `*.wiki` files into `*.md` files by attempting the
following three things:
1. Replace [Vimwiki](https://github.com/vimwiki/vimwiki) specific headings
   marker to be Markdown marker. (`= Header =` is converted to `# Header`)
2. In same fashion, replace `{{{` used in Vimwiki to the marker for code block
   in Markdown;
3. Convert links specific to Vimwiki to follow Markdown convention.
   * `[[file_link]]` will be converted to `[file_link](file_link)` 
   * `[[file_link#section_name]]` will be converted to
     `[section_name](file_name#section_name)`.

**LIMITATION**: I did not give it much thought when writing the converter, nor
am I capable to draft a full-fledged one. For the conversion of hyperlinks, be
warned that I did not consider cases where there are multiple hyperlinks on the
same line.
   
     
# Usage
Drop the script anywhere you hold your `*.wiki` files, and run it  through
commandline. It will warn you about `*.wiki` documents that it cannot handle.




## TODO
1. Make the script fail less often.
For now, the combination of `open()` and the regex-specifications is a bit
restrictive. For my use case, it fails for all files that has a single Chinese
character in it. Specifying `encoding="utf-8"` while reading the files did not
help.

Per my personal usage, I managed to convert 1900 out of 2169 `*.wiki` files that
I have accumulated over the years. I am using Vim macros to handle the rest
manually.
