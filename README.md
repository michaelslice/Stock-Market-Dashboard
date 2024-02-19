# Stock-Market-Dashboard
A financial application that displays up-to-date stock and options data, allowing users to stay updated on market trends.  

![Full_Tools](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/13dae103-28a7-4489-bafa-67e856ebdd62)

##  Menu Fundamentals

**Stock Tracker Window**

![Menu](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/83870947-1306-4788-84ea-3d208de5d5a7)

**Adding a Stock Ticker**

To add a new stock ticker to the watchlist input a stock ticker in the input frame above the 'Add Stock' button. After inputting a stock ticker click the 'Add Stock' button and a call through the yahoo finance API will be made to validate the stock ticker.

**Removing a Stock Ticker**

To remove a stock ticker from the watchlist click the 'Remove' button located on the right side of the stock name.

**Resetting The Watchlist**

By clicking the '!' button in the bottom right corner the stock watchlist will be cleared.

![Clear_Watchlist](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/4bb8133a-0f13-4c8b-9adb-10195b33265d)

Additionally a window will appear alerting the user that the watchlist has been reset.

![Reset](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/3e4aced3-a2d8-4a5b-a1a7-7b3ad1a90e57)

**Repeat Stocks**

If a specific stock is already displayed in the watchlist a new window will appear alerting the user of the repeat stock ticker.

![Repeat](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/70a35b63-dd78-400f-8557-81ca01c9211f)

## Details

**Historical Data**

By clicking the 'Details' button a new window will open with historical data for the stock ticker that is in the same row as the 'Details' button.

![Historical_Data](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/57da1ee0-fdbc-4974-92b2-101ec1e2d1c2)

##  Sectors

To access the stock Sectors click the 'Sectors' button on the top left of the main menu. After clicking the 'Sectors' button a new window will appear with buttons to sort stocks by sectors in industrials, consumer discretionary, finance, health care, real estate, miscellaneous, technology, energy, utilities, telecommunications, consumer staples, and basic materials. After clicking the desired sector the data table will present stocks for the specific sectors, and the data table will display data for the stock name, stock sector, last sale, net change, market cap, country, IPO year, volume, and industry. 

![Stock_Sectors](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/2bd877a8-28fb-41d8-8aab-a2ad2b272322)

## Screener 

The stock Screener can be accessed by clicking the 'Screener' button at the top of the main menu. By clicking the 'Screener' button a new window will appear, and the user can input two market cap values to sort stocks by. On the right side of the 'Market Cap' text input the minimum market cap value, and on the right side of the 'To' text input the highest market cap value. After inputting two market cap values click the 'Filter' button and the data table will display stocks that have market cap values that fall between the two user inputs.

![Screener](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/2468f9cc-7edb-48ea-9241-c6174edf9690)

## Stock Charts

To view the Stock Charts feature click the 'Stock Charts' button located at the top of the main menu. After clicking the 'Stock Charts' button a new window will open, on the right side of the 'Search' text the user can input a stock ticker name. On the right side of the 'Begin' text, the user can input a beginning date for the graph to start from. On the right side of the 'End' text the user can input an ending date for the graph to display the ending date for the desired stock. After entering inputs into the frames, click the 'Filter' button and a stock graph based on the user inputs will be displayed in the window. 

![Stock_Charts](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/2d20c191-f137-4e6e-ae25-eeaab39ab89b)

## Company Data

The Company Data can be accessed by clicking the 'Company Data' button. After clicking the 'Company Data' button a new window will appear, in the top right corner of the screen the user can input a stock ticker. After the stock ticker is inputted click the 'Add Stock' button and in the top right corner of the screen data for the 52-Week High, and 52-Week Low for the inputted will be displayed. Additionally, data for recent dividends, stock splits, and volume will appear.

![Company_Data](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/5b8c75e6-345c-45d7-be7a-9c71c24f032e)

## Option Prices

To access the Option Prices click the 'Option Prices' button located at the top of the main menu. After clicking the 'Option Prices' button a new window will appear, on the right side of the 'Search' text input a stock ticker. On the right side of the 'Type' the valid inputs are either a 'C' for 'Calls' or a 'P' for 'Puts'. On the right side of the 'Exp. Date' text input a desired date for the options contract expiration. On the right side of the 'Strike Price' text input the desired strike price for the option contract. After inputting values into the frames, click the 'Filter' button. Once the 'Filter' button is clicked the data table will present option quote information for the expiration, type, strike, last price, bid, ask, ask, change, % change, volume, open interest, and implied volatility.

![Option_Prices](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/2db3e33f-784a-41e3-b019-b9769bafb04e)

## Settings

To activate email notifications fill in the 'From Address' and 'To Address' fields with the preferred email address (e.g., "JohnDoe@Outlook.com"). Provide the file path of a local text file containing the email password (e.g., "C:\Users\JohnDoe\MySecretFolder\Password.txt") in the password location field. If you wish to receive email alerts, it is advisable to create a dedicated email account specifically for this application.

![Settings](https://github.com/michaelslice/Stock-Market-Dashboard/assets/110714088/a16305de-2c32-4ce0-9e27-747894cc1827)

## Instructions

Insure that Python 3 and all packages are installed.

Run dashboard.py

