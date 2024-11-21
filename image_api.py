from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 이미지 저장 경로 설정
UPLOAD_FOLDER = 'uploads'  # 업로드할 폴더 이름
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # 폴더가 없으면 생성

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload-image', methods=['POST'])
def upload_image():
    # 사용자가 업로드한 파일 가져오기
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # 파일이 없거나 파일 이름이 비어있을 경우
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 파일 저장
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return jsonify({"message": "Image uploaded successfully", "file_path": file_path}), 200

if __name__ == '__main__':
    app.run(debug=True)