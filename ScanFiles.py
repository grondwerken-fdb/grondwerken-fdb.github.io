import os

select = os.listdir("./assets/projects")

for folder in select:
    # if not os.path.exists("./_projects/" + folder + ".md"):
    with open("./_projects/" + folder + ".md", "w+") as file:
        data = folder.split("_")
        file.write("---\n")
        file.write("layout: project\n")
        file.write("link: " + folder + "\n")
        file.write("date: " + data[0].strip() + "\n")
        file.write("location: " + data[1].strip().title() + "\n")
        file.write("title: " + data[2].strip() + "\n")
        file.write("permalink: /projects/" + data[2].strip() + "\n")
        file.write("---\n")