from flask import Flask, request
import speedtest

app = Flask(__name__)

@app.route('/')
def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 10**6
    
    return {
        'download_speed': f'{download_speed:.2f} Mbps'
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0")
