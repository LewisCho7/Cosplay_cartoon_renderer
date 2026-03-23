# Cosplay_cartoon_renderer

### cosplay cartoon renderer
- cosplay_to_cartoon.py
- using opencv to process image.
- edge-preserving smoothing
- used Gaussian blur to reduce noise
- used canny edge detector
- used bilateral filter
### successful image
<img width="1443" height="994" alt="image" src="https://github.com/user-attachments/assets/30343ca6-4d86-456c-88de-1c0eac7ef4cd" />
<img width="1470" height="1024" alt="image" src="https://github.com/user-attachments/assets/dd84ed10-688a-483b-918c-c9bb8c6b8fe8" />

### unsuccessful image
<img width="1418" height="956" alt="image" src="https://github.com/user-attachments/assets/e4025a41-b5d9-4fc9-8667-bcc2ce4fd858" />

### limitations
- When *low contrast and high brightness*, canny edge detection is not working very well
- Edges are not well detected and lines are not connected which makes the image doesn't look like a cartoon style.
- Did not use morphological operations. This is because changing real human photo to cartoon is different from changing figures to cartoon.
- It looks weird when thick lines are formed near the face.
- Also when threshold is too low, more lines appear near the face which makes it awkard.
- So it will produce random results depending on the image

### cosplay cartoon renderer2
- This looks more like oil painting than cartoon
- higher threshold is used
- even though less edges are drown, I personally like this style better. It detects the scar on the face but not the other weird parts.
<img width="1437" height="992" alt="image" src="https://github.com/user-attachments/assets/5c817c8f-4975-4dca-8eb4-dbd17c681efd" />
