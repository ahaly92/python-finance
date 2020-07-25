from matplotlib import style

from services.sp500 import get_ticker_data, visualize_data

style.use('ggplot')

get_ticker_data()
visualize_data()
