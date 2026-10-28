/* Lumière Digital Co: animations */
(function () {
  const root = document.documentElement;
  const body = document.body;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const hasGSAP = typeof window.gsap !== "undefined";
  document.getElementById("year").textContent = new Date().getFullYear();

  // ---------- Split headings into words for reveal ----------
  document.querySelectorAll(".split").forEach((el) => {
    const walk = (node) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            const w = document.createElement("span"); w.className = "w";
            const i = document.createElement("span"); i.textContent = part;
            w.appendChild(i); frag.appendChild(w);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1) walk(n);
      });
    };
    walk(el);
  });

  if (!hasGSAP || reduce) {
    const i0 = document.getElementById("intro"); if (i0) i0.remove();
    body.classList.remove("is-loading");
    return;
  }

  root.classList.add("js");
  gsap.registerPlugin(ScrollTrigger);

  // ---------- Header state ----------
  const header = document.getElementById("header");
  ScrollTrigger.create({ start: 60, onUpdate: (s) => header.classList.toggle("scrolled", s.scroll() > 60) });

  // ---------- Mobile nav ----------
  const toggle = document.getElementById("navToggle");
  toggle.addEventListener("click", () => {
    const open = body.classList.toggle("nav-open");
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  });
  document.querySelectorAll(".nav a").forEach((a) => a.addEventListener("click", () => body.classList.remove("nav-open")));

  // ---------- Hero entrance (runs after intro) ----------
  const heroIn = () => {
    const tl = gsap.timeline({ defaults: { ease: "power4.out" } });
    tl.from(".header", { y: -30, opacity: 0, duration: 1.2 })
      .to(".hero .reveal-up", { opacity: 1, y: 0, duration: 1.2, stagger: 0.12 }, 0.1)
      .from(".hero-title .w > span", { yPercent: 110, duration: 1.4, stagger: 0.07 }, 0.15)
      .from(".hero-spot", { scale: 0.4, opacity: 0, duration: 2.4, ease: "power2.out" }, 0)
      .from(".scroll-cue", { opacity: 0, duration: 1 }, 1);
  };

  // ---------- Intro: light bulb in darkness ----------
  const intro = document.getElementById("intro");
  const seen = (() => { try { return sessionStorage.getItem("lumiereIntro") === "1"; } catch (e) { return false; } })();

  const endIntro = (fast) => {
    try { sessionStorage.setItem("lumiereIntro", "1"); } catch (e) {}
    gsap.to(intro, {
      opacity: 0, duration: fast ? 0.5 : 1.3, ease: "power2.inOut",
      onComplete: () => { intro.remove(); body.classList.remove("is-loading"); ScrollTrigger.refresh(); }
    });
    heroIn();
  };

  if (!intro || seen) {
    if (intro) intro.remove();
    body.classList.remove("is-loading"); heroIn();
  } else {
    const video = document.getElementById("bulbVideo");
    // bulb stays fixed in the centre: dark, flickers on, then the light glows out
    const reveal = gsap.timeline({ paused: true, onComplete: () => endIntro(false) });
    reveal.to("#introLight", { opacity: 1, scale: 1, duration: 2.8, ease: "power2.out" })
      .to("#bulb", { opacity: 0, filter: "blur(6px)", duration: 1.8, ease: "power2.inOut" }, 0.4)
      .to("#introLogo", { opacity: 1, filter: "blur(0px) drop-shadow(0 0 24px rgba(255,226,170,.35))", duration: 1.8, ease: "power2.out" }, 1.0)
      .to("#introLogo", { filter: "blur(0px) drop-shadow(0 0 8px rgba(255,226,170,.15))", duration: 1 }, "+=0.3");

    let started = false;
    const go = () => { if (!started) { started = true; reveal.play(); } };
    video.addEventListener("timeupdate", () => { if (video.duration && video.currentTime > video.duration - 0.6) go(); });
    video.addEventListener("ended", go);
    video.addEventListener("error", go, true);
    const p = video.play();
    if (p && p.catch) p.catch(go);           // autoplay blocked (e.g. low-power mode): skip straight to the reveal
    setTimeout(go, 7000);                    // safety net if the video stalls

    document.getElementById("introSkip").addEventListener("click", () => { reveal.kill(); endIntro(true); });
  }

  // ---------- Hero spotlight follows cursor ----------
  const hero = document.getElementById("hero");
  const spot = document.getElementById("heroSpot");
  if (hero && spot) hero.addEventListener("mousemove", (e) => {
    const r = hero.getBoundingClientRect();
    gsap.to(spot, { left: e.clientX - r.left, top: e.clientY - r.top, duration: 1.6, ease: "power3.out" });
  });
  if (hero) gsap.to(".hero-inner", { yPercent: 18, opacity: 0.2, ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });

  // ---------- Cursor glow ----------
  const glow = document.getElementById("cursorGlow");
  window.addEventListener("mousemove", (e) => {
    glow.classList.add("on");
    gsap.to(glow, { x: e.clientX, y: e.clientY, duration: 0.9, ease: "power3.out" });
  });

  // ---------- Magnetic buttons ----------
  document.querySelectorAll(".magnetic").forEach((btn) => {
    btn.addEventListener("mousemove", (e) => {
      const r = btn.getBoundingClientRect();
      gsap.to(btn, { x: (e.clientX - r.left - r.width / 2) * 0.25, y: (e.clientY - r.top - r.height / 2) * 0.35, duration: 0.6, ease: "power3.out" });
    });
    btn.addEventListener("mouseleave", () => gsap.to(btn, { x: 0, y: 0, duration: 0.8, ease: "elastic.out(1, .4)" }));
  });

  // ---------- Scroll reveals ----------
  gsap.utils.toArray(".split").forEach((el) => {
    if (el.closest(".hero")) return;
    gsap.from(el.querySelectorAll(".w > span"), { yPercent: 110, duration: 1.2, stagger: 0.06, ease: "power4.out", scrollTrigger: { trigger: el, start: "top 85%" } });
  });
  gsap.utils.toArray(".reveal-up").forEach((el) => {
    if (el.closest(".hero")) return;
    gsap.to(el, { opacity: 1, y: 0, duration: 1.1, ease: "power3.out", scrollTrigger: { trigger: el, start: "top 88%" } });
  });
  ScrollTrigger.batch(".reveal-card", {
    start: "top 88%",
    onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, duration: 1.1, stagger: 0.12, ease: "power3.out" })
  });

  // ---------- Parallax ----------
  gsap.utils.toArray(".parallax").forEach((el) => {
    const speed = parseFloat(el.dataset.speed || 0.1);
    gsap.fromTo(el, { y: () => 120 * speed }, { y: () => -120 * speed, ease: "none", scrollTrigger: { trigger: el, start: "top bottom", end: "bottom top", scrub: true } });
  });
  if (document.querySelector(".browser")) gsap.from(".browser", { clipPath: "inset(12% 12% 12% 12% round 14px)", duration: 1.6, ease: "power3.out", scrollTrigger: { trigger: ".work", start: "top 75%" } });

  // ---------- Process line lights up step by step ----------
  if (document.getElementById("processFill")) gsap.to("#processFill", { scaleX: 1, ease: "none", scrollTrigger: { trigger: ".process", start: "top 75%", end: "bottom 55%", scrub: true } });
  gsap.utils.toArray(".reveal-step").forEach((step, i) => {
    gsap.to(step, { opacity: 1, y: 0, duration: 1, ease: "power3.out", delay: i * 0.05, scrollTrigger: { trigger: ".process", start: `top ${78 - i * 6}%`, onEnter: () => step.classList.add("lit") } });
  });

  // ---------- Meaning: light blooms behind the word ----------
  if (document.getElementById("meaningGlow")) gsap.to("#meaningGlow", { opacity: 1, scale: 1, ease: "none", scrollTrigger: { trigger: ".meaning", start: "top 80%", end: "center center", scrub: true } });

  // ---------- Contact form: saves the enquiry to Supabase ----------
  const form = document.getElementById("contactForm");
  if (form) form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const note = document.getElementById("formNote");
    const btn = form.querySelector('button[type="submit"]');
    const f = new FormData(form);
    const v = (k) => (f.get(k) || "").toString().trim();
    if (v("website")) { form.reset(); note.textContent = "Thanks. We'll be in touch within one business day."; return; } // spam trap
    if (!v("name") || !/^\S+@\S+\.\S+$/.test(v("email"))) { note.textContent = "Please add your name and a valid email address."; return; }
    btn.disabled = true; note.textContent = "Sending…";
    try {
      const res = await fetch(form.dataset.endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", apikey: form.dataset.key, Prefer: "return=minimal" },
        body: JSON.stringify({
          name: v("name").slice(0, 200), business: v("business").slice(0, 200) || null,
          email: v("email").slice(0, 320), phone: v("phone").slice(0, 50) || null,
          package: v("package").slice(0, 50) || null, message: v("message").slice(0, 5000) || null,
        }),
      });
      if (!res.ok) throw new Error(String(res.status));
      form.reset();
      note.textContent = "Thanks. We'll be in touch within one business day.";
    } catch (err) {
      note.textContent = "Sorry, that didn't send. Please email hello@lumieredigitalco.com instead.";
    } finally {
      btn.disabled = false;
    }
  });
})();
