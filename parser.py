from re import match, search

results = []

#Example: C:\USERS_DIRECTORY\Desktop\temp_folder\my_file.txt
file_path = r''' '''
directory = ""

HTML_TAG_REGEX = r'''<a id=\"video-title\"''' #Match
HREF_START_REGEX = r'''href=\"/watch\?v=''' #Search
HREF_END_REGEX = r'''&amp''' #Search

TITLE_REGEX = r'''title=\"''' #Search

def main() -> None:
    with open(file=file_path,mode='rt',encoding='utf-8') as f:
        for line in f:
            stripped_line = line.lstrip()

            if match(HTML_TAG_REGEX,stripped_line) is not None:
                #HREF Indexes
                href_start = search(HREF_START_REGEX,stripped_line[80:])
                href_end = search(HREF_END_REGEX,stripped_line[80:])

                if href_end == None:
                    href_end = search(r"\"",stripped_line[80 + href_start.end():])

                #HREF Parse
                href = stripped_line[href_start.end() + 80:href_end.start() + 80]

                '''
                Youtube Premium gives Recommendations at the end of your Playlist.
                I filter this out by skipping videos that don't have a href field.
                '''
                if href == "":
                    continue

                full_href_link = f'https://www.youtube.com/watch?v={href}'

                #Title Indexes
                title_start = search(TITLE_REGEX,stripped_line[80:])

                #Title Parse
                title = stripped_line[title_start.end() + 80:len(stripped_line) - 3]

                #Append
                results.append([title,full_href_link])
    
    save_result()

def get_directory() -> None:
    end = file_path.rindex('\\')
    return file_path[0:end + 1]

def save_result() -> None:
    save_file = f'{directory}test_save_file.txt'
    with open(file=save_file,mode='wt',encoding='utf-8') as f:
        for entry in results:
            line = ','.join(entry)
            f.write(f'{line}\n')

if __name__ == '__main__':
    directory = get_directory()
    main()
