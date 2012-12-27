#!/usr/local/bin/python

"""
4chan-search.py
Purpose: Provides a simple search engine for 4chan
Author: Kendrick Ledet
Date: 12/26/12
"""
"""
Copyright 2012 Kendrick Ledet
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import sys, urllib2, json, time

def main():
    board = sys.argv[1].lower()
    query = sys.argv[2].strip('"')
    # Get num of board pages
    boards = json.loads(urllib2.urlopen('http://api.4chan.org/boards.json').read())['boards']
    for _board in boards:
        if _board['board'] == board:
            num_pages = int(_board['pages'])
            break
    # Begin search
    for page in range(0,num_pages):
        print 'Found on page %d:' % (page,)
        threads = json.loads(urllib2.urlopen('http://api.4chan.org/g/%d.json' % (page,)).read())['threads']
        for thread in threads:
            for post in thread['posts']:
                if ('com' in post.keys() and query in post['com']) or ('sub' in post.keys() and query in post['sub']):
                    print 'http://boards.4chan.org/%s/res/%d' % (board, post['no'])
        time.sleep(1)

if __name__ == '__main__':
    main()
