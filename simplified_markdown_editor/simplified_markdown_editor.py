# simplified_markdown_editor.py

def print_help():
    print("""
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
""")

def format_plain(text):
    return text

def format_bold(text):
    return f"**{text}**"

def format_italic(text):
    return f"*{text}*"

def format_header(text, level):
    if 1 <= level <= 6:
        return f"{'#' * level} {text}\n"
    else:
        return "The level should be within the range of 1 to 6.\n"

def format_link(label, url):
    return f"[{label}]({url})"

def format_inline_code(text):
    return f"`{text}`"

def format_ordered_list(rows):
    result = ""
    for i, row in enumerate(rows, start=1):
        result += f"{i}. {row}\n"
    return result

def format_unordered_list(rows):
    result = ""
    for row in rows:
        result += f"* {row}\n"
    return result

def main():
    formatted_text = ""
    while True:
        choice = input("Choose a formatter: > ")

        if choice == "!help":
            print_help()
        elif choice == "!done":
            with open("output.md", "w") as file:
                file.write(formatted_text)
            print("Output has been saved to output.md")
            break
        elif choice == "new-line":
            formatted_text += "\n"
        elif choice in ["plain", "bold", "italic", "inline-code"]:
            text = input("Text: > ")
            if choice == "plain":
                formatted_text += format_plain(text)
            elif choice == "bold":
                formatted_text += format_bold(text)
            elif choice == "italic":
                formatted_text += format_italic(text)
            elif choice == "inline-code":
                formatted_text += format_inline_code(text)
        elif choice == "header":
            level = int(input("Level: > "))
            text = input("Text: > ")
            formatted_text += format_header(text, level)
        elif choice == "link":
            label = input("Label: > ")
            url = input("URL: > ")
            formatted_text += format_link(label, url)
        elif choice in ["ordered-list", "unordered-list"]:
            rows = []
            while True:
                num_rows = int(input("Number of rows: > "))
                if num_rows > 0:
                    break
                else:
                    print("The number of rows should be greater than zero")
            for i in range(1, num_rows + 1):
                row = input(f"Row #{i}: > ")
                rows.append(row)
            if choice == "ordered-list":
                formatted_text += format_ordered_list(rows)
            elif choice == "unordered-list":
                formatted_text += format_unordered_list(rows)
        else:
            print("Unknown formatting type or command")

        print(formatted_text)

if __name__ == "__main__":
    main()
