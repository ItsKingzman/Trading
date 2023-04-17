from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://colab.research.google.com/github/AI4Finance-Foundation/FinRL-Tutorials/blob/master/2-Advance/FinRL_Ensemble_StockTrading_ICAIF_2020.ipynb#scrollTo=q9mKF7GGtj1g&uniqifier=2<colab_notebook_id>', 'FinRL_Ensemble_StockTrading_ICAIF_2020.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')