#!/usr/bin/python3

# Takes the number of an EulerProject exercise and generates the Python file to
# start working on it.
# Usage: euler_scraper.py <problem number>


from lxml import html
from os import path
from os import getcwd
import os
import stat
import sys
import requests
import codecs

import urllib.request

base_url = 'http://projecteuler.net/problem='

def retrieve_html(problemId):
    with urllib.request.urlopen(base_url+str(problemId)) as url:
        return url.read()

def extract_content(htmlSource):
    tree = html.fromstring(htmlSource)
    problemContent = tree.xpath('//p/text()')
    return problemContent

def main():
    if len(sys.argv) != 2:
        print('Usage: euler_scraper.py <problem number>')
        exit()

    problemId = int(sys.argv[1])
    fileName = getcwd() + '/Problem' + '%03d' % problemId + '.py'

    if path.exists(fileName):
        print('Error: %s exists already' % fileName)
        exit()

    # Get HTML source
    htmlSource = retrieve_html(problemId)

    # Get problem content
    problemContent = extract_content(htmlSource)

    outputFile = codecs.open(fileName, 'w', 'utf-8')
    outputFile.write(u'#!/usr/bin/python3\n')
    outputFile.write(u'#coding:utf8\n')
    outputFile.write(u'\n')
    outputFile.write(u'# ' + str(base_url + str(problemId)) + u'\n')
    outputFile.write(u'#\n')
    outputFile.write(u'# PROBLEM CONTENT:\n')
    for line in problemContent:
        while len(line) > 0:
            nchar = len(line)
            if len(line) > 77:
                nchar = line[:77].rfind(' ')
            if isinstance(line, str) == False:
                line = str(line, 'utf-8')
            lineToWrite = u'# ' + line[:nchar] + u'\n'
            outputFile.write(lineToWrite)
            line = line[nchar+1:]
        outputFile.write(u'#\n')

    outputFile.write(u'\n')
    outputFile.write(u'# EXPLANATION:\n')
    outputFile.write(u'\n')
    outputFile.write(u'import time\n')
    outputFile.write(u'\n')
    outputFile.write(u'def main():\n')
    outputFile.write(u'\n')
    outputFile.write(u'if __name__ == \'__main__\':\n')
    outputFile.write(u'    start = time.time()\n')
    outputFile.write(u'    main()\n')
    outputFile.write(u'    elapsed = time.time() - start\n')
    outputFile.write(u'    print(\'Solved in %.2f seconds\' % elapsed)\n')
    outputFile.close()

    stats = os.stat(fileName)
    os.chmod(fileName, stats.st_mode | 0o111)



if __name__ == "__main__":
    main()
