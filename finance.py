from matplotlib import style

from services.sp500 import compile_data

style.use('ggplot')

compile_data()
