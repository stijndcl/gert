# gert
Ghent University Examination Results Tool

GERT is a tool to create images that display the difference between the score distribution graphs handed out during the examination periods for Ghent University. We always receive the graphs some time in advance, and like to compare them to see if they got _better_ or _worse_ before we get our final marks.

I used to do this task manually for the past 9 examination periods over the course of 3 years, and quite honestly don't know why I didn't just write a tool to automate it. And so I did.

## Workflow

Parsing PDFs is difficult, and I was unable to find any libraries that could do it consistently and accurately enough. Hence, the script converts the entire PDF to an image, and uses some ~~hardcoded~~ empirically measured values to cut out & combine the graphs. This is unironically more stable than parsing the PDF.

## Installation

You may need to install `poppler` to get this tool to work. On most Linux distributions, it should already be included by default.

```shell
# Mac
$ brew install poppler

# Linux
$ sudo apt install poppler-utils
```

### So, if you're on Windows

![Jeremy Clarkson laughing at you](https://media.tenor.com/9TAVUk27odIAAAAC/jeremy-clarkson-laughing.gif)

_It's back to MSPaint for you._
