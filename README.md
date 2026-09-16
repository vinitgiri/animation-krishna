# 🦚 Krishna Particle Animation — Web Version

A browser-ready version of the Krishna particle animation, built with **HTML5 Canvas, CSS and JavaScript**.

## ✨ Features

- Krishna image forms from scattered particles
- Smooth particle movement
- Glow and sparkle effects
- Final image fade-in
- Animated **Vinit Kumar Giri** name
- Beautiful circular mute/unmute control
- Music starts muted
- Fully responsive vertical layout
- No framework or build step required
- Works directly on Vercel

## 📁 Required files

```text
Krishna/
├── index.html
├── krishna.png
├── song.mp3
└── README.md
```

> `krishna.png` and `song.mp3` are required assets. Keep both in the same folder as `index.html`.

## 🚀 Run locally

Because the browser loads local image/audio assets, it is better to use a small local server.

### VS Code Live Server

Open the folder in VS Code and use the **Live Server** extension.

### Python server

```bash
python -m http.server 5500
```

Then open:

```text
http://localhost:5500
```

## 🌐 Deploy on Vercel

This is now a static web project, so Vercel can serve it directly.

1. Push the project to GitHub.
2. Import the repository into Vercel.
3. Framework preset: **Other** / static site.
4. Build command: leave empty.
5. Output directory: leave empty or use the project root.
6. Deploy.

No `npm install` or `npm run dev` is required.

## 🎵 Music

Music is intentionally muted when the page opens because browsers restrict automatic audio playback.

Click the circular speaker button in the bottom-right corner to start the song.

## 🖼️ Customization

### Change the name

Inside `index.html`:

```html
<div id="name">Vinit Kumar Giri</div>
```

### Change particle density

Inside the JavaScript:

```javascript
const GAP = 5;
```

Use a smaller value such as `3` for more particles and more image detail.

### Change image size

```javascript
const MAX_W = 400;
const MAX_H = 650;
```

## 👨‍💻 Author

**Vinit Kumar Giri**

GitHub: https://github.com/vinitgiri

## 📜 License

Created for educational and  

