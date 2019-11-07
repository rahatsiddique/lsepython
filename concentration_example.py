#### helpful template, all this is available from https://github.com/econpy/search_engine_hhi/blob/master/analysis.py

from pandas import read_csv,DataFrame,DatetimeIndex


def makeDataFrame(countryname):
    csvfile = 'data/search_engine-%s-monthly-200807-201304.csv' % countryname
    dframe = read_csv(csvfile, index_col=0)
    dframe.index = DatetimeIndex(dframe.index)
    return dframe


def get_hhi(dframe):
    HHI_VALS = []
    for idx in dframe.iterrows():
        shares = [s for s in idx[1] if s > 0]
        numfirms = len(shares)
        sqr_shares = [s*s for s in shares]
        hhi_val = sum(sqr_shares)
        HHI_VALS.append({'month': idx[0], 'hhi': hhi_val})
    dframeHHI = DataFrame(HHI_VALS)
    dframeHHI.index = DatetimeIndex(dframeHHI.pop('month'))
    return dframeHHI['hhi']

countries = ['US', 'CA', 'GB', 'FR', 'CN', 'RU', 'DE']
data = {country: get_hhi(makeDataFrame(country)) for country in countries}
bigdf = DataFrame(data)
bigdf.plot()
