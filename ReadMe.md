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

Please suggest if there is a pandoc parameter that I missed, which does
everything perfectly.
   
     
# Usage
Drop the script anywhere you hold your `*.wiki` files, and run it  through
commandline. It will warn you about `*.wiki` documents that it cannot handle.




## TODO
1. Make the script fail less often.
For now, the combination of `open()` and the regex-specifications is a bit
restrictive. For my use case, it fails for all files that has a single Chinese
character in it. Specifying `encoding="utf-8"` while reading the files did not
help.

# Reflection 

As a New Year Resolution, I have been wanting to convert all my `*.wiki` files
into Markdown syntax for a good number of months. Things started when I learned
how use Github Pages, which can render static website from `*.md` files.

Per my personal usage, I managed to convert 1900 out of 2169 `*.wiki` files that
I have accumulated over the years. I am using Vim macros to handle the rest
manually.

## Simple guide to "migrate" from Vimwiki to Markdown syntax
After one has converted all the existing `*.wiki` files into `*.md`, here are
two key steps to "tell Vim" about the migration.
1. When declaring the Wikis in `~/.vimrc`, include two new keys to specify the
   markdwon syntax for the **files to be created** by Vimwiki in those Wikis. A
   minimum example goes as follows (credits to @Nudin in [this
   post](https://github.com/vimwiki/vimwiki/issues/576)):
   ```vim
   set nocompatible
   filetype plugin indent on
   syntax on

   call plug#begin('~/.vim/plugged')
   Plug 'vimwiki/vimwiki'
   call plug#end()

   " vimwiki
   let wiki_1 = {}
   let wiki_1.path = '~/vimwiki/'
   let wiki_1.syntax = 'markdown'
   let wiki_1.ext = '.md'

   let g:vimwiki_list = [wiki_1]
   ```
   By the end of the day, files created in `wiki_1` fill have file extension as
   `*.md`, and their `filtype` will also be Vimwiki.
   
2. More importanlty, one need to tell the Vimwiki Plugin to handle all `*.md`
   files, to streamline the editing experience. (Otherwise, I tend to press `=`
   for prompting a line to be the header, only to get `= Header =` in return,
   which was following the original Vimwiki convesion.) The following line
   does the job of appointing Vimwiki to deligate all affairs for Markdown
   files (again, credits to @Nudin in [this
   post](https://github.com/vimwiki/vimwiki/issues/576)):
   ```vim
   let g:vimwiki_ext2syntax = {'.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
   ```
    
Lastly, a bit of icing on the cake is to *render* the Markdown syntaxes
correctly. One will need to play with the following setting, with options
ranging from `0`, `1` and `2`:
    ```vim
    setlocal conceallevel=2
    ```
   


## Personal views
[Vimwiki](https://github.com/vimwiki/vimwiki) is by far the best "Markdown"
editor upon the aforementioned configuration: it auto-completes 
