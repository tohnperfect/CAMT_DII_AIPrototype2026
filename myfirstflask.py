from flask import Flask,  flash, redirect, request, render_template, make_response, url_for
import json
import sys 

app = Flask(__name__)

@app.route("/") 
def helloworld():
    return "Hello, World!"

@app.route("/name") 
def name():
    return "Thanapong Intharah IDXXXXX"

@app.route("/showhtmlresponse") 
def showhtmlresponse():
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Thanapong Intharah — Resume</title>
<style>
    :root {
        --ink: #1a1a1a;
        --muted: #666;
        --accent: #0f4c81;
        --line: #e5e5e5;
        --bg: #ffffff;
        --soft: #f7f7f5;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
        color: var(--ink);
        background: var(--soft);
        line-height: 1.55;
        font-size: 15px;
        padding: 40px 20px;
    }
    .page {
        max-width: 880px;
        margin: 0 auto;
        background: var(--bg);
        padding: 56px 64px;
        box-shadow: 0 2px 24px rgba(0,0,0,0.06);
        border-radius: 6px;
    }
    header {
        border-bottom: 2px solid var(--accent);
        padding-bottom: 20px;
        margin-bottom: 28px;
    }
    h1 {
        font-size: 32px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 4px;
    }
    .title {
        font-size: 16px;
        color: var(--accent);
        font-weight: 500;
        margin-bottom: 12px;
    }
    .contact {
        font-size: 13px;
        color: var(--muted);
        display: flex;
        flex-wrap: wrap;
        gap: 14px;
    }
    .contact span::before {
        content: "•";
        margin-right: 14px;
        color: var(--line);
    }
    .contact span:first-child::before { content: ""; margin: 0; }
    section { margin-bottom: 26px; }
    h2 {
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: var(--accent);
        font-weight: 700;
        margin-bottom: 12px;
        padding-bottom: 6px;
        border-bottom: 1px solid var(--line);
    }
    .summary { font-size: 14.5px; color: #333; }
    .item { margin-bottom: 16px; }
    .item:last-child { margin-bottom: 0; }
    .item-head {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 4px;
    }
    .item-title { font-weight: 600; font-size: 15px; }
    .item-org { color: var(--muted); font-size: 14px; }
    .item-date {
        font-size: 13px;
        color: var(--muted);
        font-variant-numeric: tabular-nums;
    }
    .item-desc { font-size: 14px; color: #333; margin-top: 4px; }
    ul.bullets { list-style: none; padding-left: 0; margin-top: 6px; }
    ul.bullets li {
        position: relative;
        padding-left: 16px;
        margin-bottom: 4px;
        font-size: 14px;
        color: #333;
    }
    ul.bullets li::before {
        content: "▸";
        position: absolute;
        left: 0;
        color: var(--accent);
    }
    .skills-grid {
        display: grid;
        grid-template-columns: 160px 1fr;
        gap: 10px 18px;
        font-size: 14px;
    }
    .skills-grid dt { font-weight: 600; color: var(--ink); }
    .skills-grid dd { color: #333; }
    .awards { font-size: 14px; }
    .awards li { margin-bottom: 6px; }
    @media (max-width: 640px) {
        body { padding: 0; }
        .page { padding: 32px 24px; border-radius: 0; box-shadow: none; }
        h1 { font-size: 26px; }
        .skills-grid { grid-template-columns: 1fr; gap: 4px 0; }
        .skills-grid dt { margin-top: 8px; }
    }
    @media print {
        body { background: white; padding: 0; }
        .page { box-shadow: none; padding: 32px; }
    }
</style>
</head>
<body>
<div class="page">
    <header>
        <h1>Thanapong Intharah, Ph.D.</h1>
        <div class="title">Associate Professor &middot; AI Researcher &middot; Co-Founder</div>
        <div class="contact">
            <span>Khon Kaen University</span>
            <span>Khon Kaen, Thailand</span>
            <span>email@example.com</span>
            <span>linkedin.com/in/...</span>
        </div>
    </header>
 
    <section>
        <h2>Profile</h2>
        <p class="summary">
            Associate Professor of Statistics at Khon Kaen University and co-founder of Tensor Mill Co., Ltd.,
            bridging academic research and industry through applied AI in healthcare and intelligent surveillance.
            Research focuses on computer vision, machine learning, and deep learning, with deployed systems
            serving 250+ hospitals across Thailand and Laos.
        </p>
    </section>
 
    <section>
        <h2>Education</h2>
        <div class="item">
            <div class="item-head">
                <div>
                    <span class="item-title">Ph.D. in Computer Science</span>
                    <span class="item-org"> &middot; University College London (UCL)</span>
                </div>
                <span class="item-date">United Kingdom</span>
            </div>
        </div>
        <div class="item">
            <div class="item-head">
                <div>
                    <span class="item-title">M.Sc. in Machine Learning</span>
                    <span class="item-org"> &middot; University College London (UCL)</span>
                </div>
                <span class="item-date">United Kingdom</span>
            </div>
        </div>
        <div class="item">
            <div class="item-head">
                <div>
                    <span class="item-title">M.Sc. in Computer Science</span>
                    <span class="item-org"> &middot; Chulalongkorn University</span>
                </div>
                <span class="item-date">Thailand</span>
            </div>
        </div>
    </section>
 
    <section>
        <h2>Experience</h2>
        <div class="item">
            <div class="item-head">
                <span class="item-title">Associate Professor, Department of Statistics</span>
                <span class="item-date">Present</span>
            </div>
            <div class="item-org">Faculty of Science, Khon Kaen University</div>
            <ul class="bullets">
                <li>Principal Investigator, KKU Visual Intelligence Laboratory (VILab).</li>
                <li>Lead research and graduate supervision in computer vision, ML, and healthcare AI.</li>
                <li>Teach data science, data mining, and machine learning at undergraduate and graduate level.</li>
            </ul>
        </div>
        <div class="item">
            <div class="item-head">
                <span class="item-title">Co-Founder &amp; Technical Lead</span>
                <span class="item-date">Present</span>
            </div>
            <div class="item-org">Tensor Mill Co., Ltd.</div>
            <ul class="bullets">
                <li>Develop and deploy BiTNet/ATra — an AI ultrasound platform for cholangiocarcinoma screening.</li>
                <li>Apply computer vision to CCTV and healthcare workflows for industry partners.</li>
            </ul>
        </div>
    </section>
 
    <section>
        <h2>Selected Research &amp; Projects</h2>
        <div class="item">
            <div class="item-title">BiTNet / ATra — AI Ultrasound Screening Platform</div>
            <div class="item-desc">
                EfficientNet-B5 + Random Forest pipeline with knowledge distillation to MobileNetV3-Small
                for offline deployment. Deployed across 250+ hospitals; patent filed 2025.
            </div>
        </div>
        <div class="item">
            <div class="item-title">OV-RDT &mdash; Liver Fluke Screening from Rapid Diagnostic Tests</div>
            <div class="item-desc">
                End-to-end AI screening system; over 100,000 strips analyzed via integrated dashboard.
            </div>
        </div>
        <div class="item">
            <div class="item-title">Participatory AI Shield &mdash; Deepfake &amp; Disinformation Detection</div>
            <div class="item-desc">
                Multimodal Thai-language pipeline (EfficientNet + Wav2Vec) with crowdsourced consensus routing.
            </div>
        </div>
    </section>
 
    <section>
        <h2>Skills</h2>
        <dl class="skills-grid">
            <dt>Research</dt>
            <dd>Computer Vision, Deep Learning, Medical Imaging, Knowledge Distillation, XAI</dd>
            <dt>Frameworks</dt>
            <dd>PyTorch, TensorFlow, scikit-learn, OpenCV</dd>
            <dt>Languages</dt>
            <dd>Python, R, JavaScript, SQL</dd>
            <dt>Deployment</dt>
            <dd>Edge AI (MobileNet, AIoT), Flask APIs, Docker, Cloud GPU</dd>
            <dt>Languages (Spoken)</dt>
            <dd>Thai (native), English (fluent)</dd>
        </dl>
    </section>
 
    <section>
        <h2>Selected Awards &amp; Recognition</h2>
        <ul class="bullets awards">
            <li>Silver Medal, International Exhibition of Inventions Geneva (2024)</li>
            <li>ASEAN Digital Award (2024)</li>
            <li>Medical AI Pitching Award, IEEE ISBI (2024)</li>
            <li>Royal Academy of Engineering Fellowship (2020)</li>
            <li>NIA Innovation Award (2021)</li>
        </ul>
    </section>
</div>
</body>
</html>"""

@app.route('/receive_get',methods=['GET']) 
def web_service_API_GET():

    msg = request.args.get('msg')
    name = request.args.get('name')
    
    print(f'the input message from GET is {msg} from {name}.')
    
    return f'{msg} from {name} received!'

@app.route('/request_POST',methods=['POST']) 
def web_service_API_POST():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload) # ทำ json
    print(inmessage)
    json_data = json.dumps({'y': 'POST received!'}) # ส่งกลับไปว่าได้รับเเล้ววว
    return json_data
    

if __name__ == "__main__":   # run code 
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001
    