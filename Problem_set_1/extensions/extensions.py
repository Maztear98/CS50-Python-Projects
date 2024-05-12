# Ask user to enter files with file extensions at the end. Return this input as a mime type

file = input("File name: ").strip().casefold()

# Split file name and the extension

extension = file.rsplit(".",1)[-1]

# assign a case if extension was not added

if extension:
    file_type = extension

else:
    file_type = ""
    print("application/octet-stream")


match file_type:
    case "gif"|"png":
        print(f"image/{extension}")
    case "jpeg"|"jpg":
        print("image/jpeg")
    case "pdf"| "zip":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")



