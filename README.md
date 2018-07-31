CSV Consolidate
======


## Overview
Reads all csv files from a work directory and its child directories, and consolidates their contents
into a single directory.  Import the data from the generated CSV file to a Spreadsheet file, preferably Google Spreadsheets.


## Running

`python consolidate.py [work_dir] [output_filename]`

where

`work_dir` - the parent directory where your csv files are located
`output_filename` - where the consolidated values will be saved


### (Current) Assumptions

You're using Shopify and your CSV files have the following fieldnames:

- `Buyer Fullname`
- `Buyer Address 1`
- `Buyer Address 2`
- `Buyer City`
- `Buyer State`
- `Buyer Zip`
- `Buyer Country`
- `Buyer Phone Number`
- `Buyer Email`


### Output

A csv file containing the following fields and the previous fields their values are based upon:

- `full_name`: `Buyer Fullname`
- `address`: `Buyer Address 1`, `Buyer Address 2`, `Buyer City`, `Buyer State`
- `zip`: `Buyer Zip`
- `country`: `Buyer Country`
- `contact_number`: `Buyer Phone Number`
- `email`: `Buyer Email`


### Removing duplicates
Follow this [link](https://developers.google.com/apps-script/articles/removing_duplicates), to remove duplicates in your spreadsheet.


### Now What

Read the backstory.


## Configuration

Tested on:
Python 2.7.12


## Backstory

When I quit my comfortable and stable job as a Software Engineer two months ago, I was fully intent on experimenting with various technologies, fields, ideas, business opportunities--essentially experiences that I'd never get to have if I were to stay in my comfort zone.  Within the past two months, however, I found myself just drifting through the winds and wanting to start again, but only doing what I've always been doing minus the commute--eat, sleep, code.

Hence as part of my quest redeem myself and explore what life has to offer, I've become a Retail Associate. Yes, that's a more fancy and CV-friendly title for "a person who stands by a shop waiting for customers to come".

Yes, I'm now employed again.  But no longer in a fancy office with lots of space and free food--this time, I'm now employed at an antique shop--full of coins hundreds of years old, with half-century old Coca-Cola bottles whose previous owners resisted the urge to drink, vinyl records, dolls that would not have been terrifying had they not been as old as my great-grandmother. Oh, don't forget the ethnic Filipino bolos and knives which have now all taken fine patina.

Yeah, I didn't realize I fancy antiques until now.

31-July-2018, Tuesday. My first day at work.
I got in through a friend from my mountaineering org who mentioned she was leaving hence there'd now be an opening, which I apparently quickly grabbed.  She described her experience as follows:
- Lots of free time since customers rarely come
- There's a fast internet connection
- You get paid even when you didn't get to sell anything
- Aside from manning the booth, my friend "encoded data in a spreadsheet"

With these in mind, I figured I can:
- Still code while manning the shop, and earn money while doing so
- I'd get to experience a whole new environment--Yay, antiques!
- Challenge myself to figure out ways to gain more customers in the shop
- Learn how they run the business--ebay, shopify, physical shop, google search rankings (stuff I've been wanting to try myself! (except the physical shop))

Yada yada yada.  Turns out, my friend didn't finish "encoding data in a spreadsheet" and I've now inherited the job.
And turns out, I'd have to copy and paste certain values from 200 CSV Files, totalling 1827 lines that I had to look at...

LOL. Hell naw.
I'm all for experience, but only for experiences that makes my brain grow at least a bit.

And that's why I made this repo.


## Limitations

No security checks. They who intend to use malicious data will only end up harming themselves.


## [Planned] Future Work
1. Integration with google spreadsheet
2. Automate removal of duplicates
3. Let user select fields to include
4. Let user customize output fields
