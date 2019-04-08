# File: Ch12-Sun.py
# Description:

def main():
    name = input("Enter your name: ")
    description = input("Describe yourself: ")
    for retry in range(3):
        try:
            filename = open("Your_personal_web", 'w')
        except IOError as e:
            print(e)
        filename.write(html_code(name, description))
        filename.close()
        print("success")
    


def html_code(name, description):
    return """
    <html>
        <head>
        </head>
        <body>
            <center>
                <h1>"""+name+"""</h1>
            </center>
            <hr />"""+description+"""<hr />
        </body>
    </html>
"""

main()