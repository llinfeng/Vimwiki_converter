# Pyhton 3.7 or so
# Nothing fancy in this script.

import re

from pathlib import Path

# Collect files in the "home folder", or the directory that is nexted in "home folder";
# "Home folder" is where this script lives.
txt_files = list(Path(".").rglob("*.[tT][xX][tT]"))
wiki_files = list(Path(".").rglob("*.[wW][iI][kK][iI]"))
md_files = list(Path(".").rglob("*.[mM][dD]"))

def dup_convert_md_from_wiki(file_name_ending_with_wiki):

    try:
        name_except_for_extension = file_name_ending_with_wiki[:-5]
        input_name = file_name_ending_with_wiki
        output_name = name_except_for_extension + '.md'

        f = open(input_name, 'r')
        lines = f.readlines()
        f.close()

        f = open(output_name, 'w')

        H_marker_start = re.compile(r'^=')


        # Fix the headings and {{{ markers for code-block
        for line in lines:
            # Check if the line is Header, or marker for code-block
            if (H_marker_start.search(line)):
                total_markers = line.count('=')
                H_level = total_markers // 2
                header_content = line[H_level:-(H_level+1)]
                header_line = "#" * H_level + header_content + "\n"
                f.write(header_line)
            elif ('{{{' in line):
                start = line.find('{{{')
                end = start + 3
                left_content = line[:start]
                right_content = line[end:]
                the_line = left_content + '```' + right_content
                f.write(the_line)
            elif ('}}}' in line):
                code_marker_start = line.find('}}}')
                end = start + 3
                left_content = line[:start]
                right_content = line[end:]
                the_line = left_content + '```' + right_content
                f.write(the_line)
            else:
                f.write(line)
        f.close()

        f = open(output_name, 'r')
        first_pass_lines = f.readlines()
        f.close()

        # Now, try to catch the links, then can be of form:
        # 1. [[Link_to_a_file]]
        # 2. [[File_name_as_link#Section name]]
        # The output:
        # 1. ==> [Link_to_a_file](Link_to_a_file) <== if there is no `#` in the line, just use the content.
        # 2. ==> [Section name](--string-content--)
        f = open(output_name, 'w')
        link_marker = re.compile(r'\[\[.*\]\]')
        for line in first_pass_lines:
            # Here, we deal with one occurance of the link. Will employ a macro for long-time fixing.
            # Those with `#` is harder to clean. Shall prioritize replacing it first.
            if link_marker.search(line):
                if "#" in line:
                    source_string = line
                    regex_pattern_plaintext = r'\[\[.*\]\]'
                    # Find start and ending slot of the matched regex
                    start = re.search(regex_pattern_plaintext, source_string).start()
                    left_content = source_string[:start]
                    end = re.search(regex_pattern_plaintext, source_string).end()
                    right_content = source_string[end:]
                    marker_content = source_string[start+2:end-2]
                    # Compose the new link
                    sharp_index = marker_content.find("#")
                    section_name = marker_content[ sharp_index + 1 : ]
                    link_meat = "[{section}]({full_address})".format(section = section_name, full_address = marker_content)
                    # Compose the line.
                    f.write(left_content + link_meat + right_content)
                else:
                    source_string = line
                    regex_pattern_plaintext = r'\[\[.*\]\]'
                    # Find start and ending slot of the matched regex
                    start = re.search(regex_pattern_plaintext, source_string).start()
                    left_content = source_string[:start]
                    end = re.search(regex_pattern_plaintext, source_string).end()
                    right_content = source_string[end:]
                    marker_content = source_string[start+2:end-2]
                    # Compose the full line
                    f.write(left_content + "[{}]({})".format(marker_content, marker_content) + right_content)
            else:
                f.write(line)
    except:
        return(file_name_ending_with_wiki)

def dup_convert_md_from_wiki(file_name_ending_with_wiki):
    name_except_for_extension = file_name_ending_with_wiki[:-5]
    input_name = file_name_ending_with_wiki
    output_name = name_except_for_extension + '.md'

    f = open(input_name, 'r')
    lines = f.readlines()
    f.close()

    f = open(output_name, 'w')

    H_marker_start = re.compile(r'^=')


    # Fix the headings and {{{ markers for code-block
    for line in lines:
        # Check if the line is Header, or marker for code-block
        if (H_marker_start.search(line)):
            total_markers = line.count('=')
            H_level = total_markers // 2
            header_content = line[H_level:-(H_level+1)]
            header_line = "#" * H_level + header_content + "\n"
            f.write(header_line)
        elif ('{{{' in line):
            start = line.find('{{{')
            end = start + 3
            left_content = line[:start]
            right_content = line[end:]
            the_line = left_content + '```' + right_content
            f.write(the_line)
        elif ('}}}' in line):
            code_marker_start = line.find('}}}')
            end = start + 3
            left_content = line[:start]
            right_content = line[end:]
            the_line = left_content + '```' + right_content
            f.write(the_line)
        else:
            f.write(line)
    f.close()

    f = open(output_name, 'r')
    first_pass_lines = f.readlines()
    f.close()

    # Now, try to catch the links, then can be of form:
    # 1. [[Link_to_a_file]]
    # 2. [[File_name_as_link#Section name]]
    # The output:
    # 1. ==> [Link_to_a_file](Link_to_a_file) <== if there is no `#` in the line, just use the content.
    # 2. ==> [Section name](--string-content--)
    f = open(output_name, 'w')
    link_marker = re.compile(r'\[\[.*\]\]')
    for line in first_pass_lines:
        # Here, we deal with one occurance of the link. Will employ a macro for long-time fixing.
        # Those with `#` is harder to clean. Shall prioritize replacing it first.
        if link_marker.search(line):
            if "#" in line:
                source_string = line
                regex_pattern_plaintext = r'\[\[.*\]\]'
                # Find start and ending slot of the matched regex
                start = re.search(regex_pattern_plaintext, source_string).start()
                left_content = source_string[:start]
                end = re.search(regex_pattern_plaintext, source_string).end()
                right_content = source_string[end:]
                marker_content = source_string[start+2:end-2]
                # Compose the new link
                sharp_index = marker_content.find("#")
                section_name = marker_content[ sharp_index + 1 : ]
                link_meat = "[{section}]({full_address})".format(section = section_name, full_address = marker_content)
                # Compose the line.
                f.write(left_content + link_meat + right_content)
            else:
                source_string = line
                regex_pattern_plaintext = r'\[\[.*\]\]'
                # Find start and ending slot of the matched regex
                start = re.search(regex_pattern_plaintext, source_string).start()
                left_content = source_string[:start]
                end = re.search(regex_pattern_plaintext, source_string).end()
                right_content = source_string[end:]
                marker_content = source_string[start+2:end-2]
                # Compose the full line
                f.write(left_content + "[{}]({})".format(marker_content, marker_content) + right_content)
        else:
            f.write(line)

# Raw loop, apply the parser
files_not_converting = []

for file in wiki_files:
    filename = str(file)
    if dup_convert_md_from_wiki(filename) != None:
        files_not_converting.append(dup_convert_md_from_wiki(filename))

if len(files_not_converting) > 0:
    print("Here is a list of files that did not convert:")
    for item in files_not_converting:
        print(item)
else:
    print("Finished!")
