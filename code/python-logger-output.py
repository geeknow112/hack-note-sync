# ```python
import logging

# ログの設定
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# ログの出力
logging.debug('Debugログ')
logging.info('Infoログ')
logging.warning('Warningログ')
logging.error('Errorログ')
logging.critical('Criticalログ')
# ```


# ```python
import logging

# ログの設定
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='example.log')

# ログの出力
logging.debug('Debugログ')
logging.info('Infoログ')
logging.warning('Warningログ')
logging.error('Errorログ')
logging.critical('Criticalログ')
# ```

