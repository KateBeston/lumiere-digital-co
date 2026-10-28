"""Generates the static HTML pages. Run: python3 _source/build_pages.py (from the repo root).
Shared header/footer live here; page content lives in PAGES below."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://lumieredigitalco.com"
NAV = [("services.html", "Services"), ("work.html", "Work"), ("packages.html", "Packages"), ("about.html", "About")]

def head(title, desc, path):
    url = f"{SITE}/{'' if path == 'index.html' else path}"
    return f"""<!doctype html>
<html lang="en-AU">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/icon-512.png">
  <meta property="og:locale" content="en_AU">
  <meta name="theme-color" content="#12191c">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"ProfessionalService","name":"Lumière Digital Co","url":"{SITE}/","logo":"{SITE}/assets/img/icon-512.png","description":"Websites with online booking and payments for Brisbane small businesses.","areaServed":"Brisbane, Queensland, Australia","email":"hello@lumieredigitalco.com"}}
  </script>
</head>"""

def header(active):
    links = "\n      ".join(f'<a href="{h}"{" class=\"active\" aria-current=\"page\"" if h == active else ""}>{l}</a>' for h, l in NAV)
    return f"""
  <header class="header" id="header">
    <a href="index.html" class="header-logo" aria-label="Lumière Digital Co home">
      <img src="assets/img/lumiere-wordmark-reversed.svg" alt="Lumière Digital Co" width="132" height="44">
    </a>
    <nav class="nav" id="nav">
      {links}
      <a href="contact.html" class="btn btn-sm magnetic">Start a project</a>
    </nav>
    <button class="nav-toggle" id="navToggle" aria-label="Open menu"><span></span><span></span></button>
  </header>
"""

FOOTER = """
  <section class="cta-band">
    <div class="wrap cta-band-inner">
      <h2 class="split">Ready to step <em>into the light?</em></h2>
      <a href="contact.html" class="btn magnetic">Start your project</a>
    </div>
  </section>

  <footer class="footer">
    <div class="wrap footer-inner">
      <img src="assets/img/lumiere-logo-reversed.svg" alt="Lumière Digital Co" class="footer-logo">
      <nav class="footer-links"><a href="index.html">Home</a><a href="services.html">Services</a><a href="work.html">Work</a><a href="packages.html">Packages</a><a href="about.html">About</a><a href="contact.html">Contact</a></nav>
      <div class="footer-bottom">
        <span>© <span id="year"></span> Lumière Digital Co · Brisbane, Queensland</span>
        <span><a href="mailto:hello@lumieredigitalco.com">hello@lumieredigitalco.com</a></span>
        <span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · Aurella Group Pty Ltd · ABN 70 649 742 423</span>
      </div>
    </div>
  </footer>

  <div class="cursor-glow" id="cursorGlow" aria-hidden="true"></div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""

INTRO = """
  <div class="intro" id="intro" aria-hidden="true">
    <div class="intro-light" id="introLight"></div>
    <div class="bulb" id="bulb">
      <video id="bulbVideo" muted playsinline preload="auto">
        <source src="assets/video/bulb.webm" type="video/webm">
        <source src="assets/video/bulb.mp4" type="video/mp4">
      </video>
    </div>
    <img class="intro-logo" id="introLogo" src="assets/img/lumiere-logo-reversed.svg" alt="">
    <button class="intro-skip" id="introSkip" type="button">Skip intro</button>
  </div>
"""

def page_hero(eyebrow, title, lead):
    return f"""
    <section class="hero hero-page" id="hero">
      <div class="hero-spot" id="heroSpot"></div>
      <div class="hero-grain"></div>
      <div class="wrap hero-inner">
        <p class="eyebrow reveal-up">{eyebrow}</p>
        <h1 class="hero-title split">{title}</h1>
        <p class="hero-lead reveal-up">{lead}</p>
      </div>
    </section>"""

MARQUEE = """
    <div class="marquee" aria-hidden="true">
      <div class="marquee-track">
        <span>Websites</span><i>✦</i><span>Online bookings</span><i>✦</i><span>Payments</span><i>✦</i><span>Google visibility</span><i>✦</i><span>Care plans</span><i>✦</i>
        <span>Websites</span><i>✦</i><span>Online bookings</span><i>✦</i><span>Payments</span><i>✦</i><span>Google visibility</span><i>✦</i><span>Care plans</span><i>✦</i>
      </div>
    </div>"""

SERVICE_CARDS = """
        <div class="services">
          <article class="service reveal-card"><span class="service-num">01</span><h3>Websites that look the part</h3><p>Custom-designed, mobile-first sites that make a strong first impression and turn visitors into customers.</p></article>
          <article class="service reveal-card"><span class="service-num">02</span><h3>Online booking and payments</h3><p>Clients book, pay deposits and buy gift cards any time of day. We set up Square or Fresha and connect it to your site.</p></article>
          <article class="service reveal-card"><span class="service-num">03</span><h3>Found on Google</h3><p>Built for search from day one, with your Google Business Profile set up so local customers can find you.</p></article>
          <article class="service reveal-card"><span class="service-num">04</span><h3>Cared for after launch</h3><p>Price changes, new photos, seasonal updates. Send a message and it's done, with no logins to remember.</p></article>
        </div>"""

WORK_VISUAL = """
        <div class="work-visual">
          <div class="browser parallax" data-speed="0.12">
            <div class="browser-bar"><span></span><span></span><span></span><em>yourbusiness.com.au</em></div>
            <div class="browser-screen">
              <img src="https://images.unsplash.com/photo-1611173622933-91942d394b04?w=1200&q=80&auto=format&fit=crop" alt="Concept website for a pet grooming studio" loading="lazy">
              <div class="browser-overlay"><span>Algester, Brisbane</span><strong>Welcome to the grooming house</strong><em>Book now</em></div>
            </div>
          </div>
          <div class="phone parallax" data-speed="-0.08">
            <img src="https://images.unsplash.com/photo-1528846104175-4fd300ee59da?w=600&q=80&auto=format&fit=crop" alt="" loading="lazy">
            <div class="phone-book"><small>Full groom</small><strong>Choose a time</strong><span>Tue 10:00</span><span class="on">Tue 1:30</span><span>Wed 9:00</span></div>
          </div>
        </div>"""

PACKAGES = """
        <div class="packages">
          <article class="package reveal-card">
            <h3>Essential</h3>
            <p class="price"><small>from</small> $500</p>
            <p class="package-desc">A polished website that makes your business look as good as it is.</p>
            <ul><li>Custom-designed website</li><li>Services, prices and gallery</li><li>Contact form and Google Map</li><li>Mobile-friendly and fast</li><li>Search-ready set-up</li><li>Two rounds of revisions</li></ul>
            <a href="contact.html" class="btn btn-ghost magnetic">Get started</a>
          </article>
          <article class="package package-featured reveal-card">
            <span class="badge">Most popular</span>
            <h3>Bookings</h3>
            <p class="price"><small>from</small> $1,000</p>
            <p class="package-desc">Everything in Essential, plus customers can book and pay online any time.</p>
            <ul><li>Everything in Essential</li><li>Multi-page website</li><li>Online booking set up for you</li><li>Deposits, payments and gift cards</li><li>Instagram gallery and FAQ</li><li>Google Business Profile set-up</li></ul>
            <a href="contact.html" class="btn magnetic">Get started</a>
          </article>
          <article class="package reveal-card">
            <h3>Care plan</h3>
            <p class="price"><small>from</small> $50<span>/month</span></p>
            <p class="package-desc">Peace of mind after launch. We keep your site fresh, so you don't have to.</p>
            <ul><li>Content and price updates</li><li>New photos and seasonal changes</li><li>Hosting and uptime checks</li><li>Priority support</li><li>Cancel any time with 30 days' notice</li></ul>
            <a href="contact.html" class="btn btn-ghost magnetic">Ask about care</a>
          </article>
        </div>"""

PROCESS = """
    <section class="section section-deep" id="process">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow reveal-up">How it works</p>
          <h2 class="split">From first chat to live <em>in about a week.</em></h2>
        </div>
        <div class="process">
          <div class="process-line"><span id="processFill"></span></div>
          <div class="step reveal-step"><span class="step-dot"></span><p class="step-num">01</p><h3>Discover</h3><p>A quick chat about your business, your customers and what you need your site to do.</p></div>
          <div class="step reveal-step"><span class="step-dot"></span><p class="step-num">02</p><h3>Design</h3><p>We design your site around your brand and show you a preview to react to.</p></div>
          <div class="step reveal-step"><span class="step-dot"></span><p class="step-num">03</p><h3>Build and connect</h3><p>We build it, set up your booking and payments, and connect your domain.</p></div>
          <div class="step reveal-step"><span class="step-dot"></span><p class="step-num">04</p><h3>Launch</h3><p>Your site goes live, and we show you how everything works. Then you get back to business.</p></div>
        </div>
      </div>
    </section>"""

PAGES = {}

PAGES["index.html"] = ("Lumière Digital Co | Websites with online booking for Brisbane businesses",
 "Lumière Digital Co designs professional websites with online booking and payments for Brisbane small businesses. Live in a week, set up for you.",
 True, f"""
    <section class="hero" id="hero">
      <div class="hero-spot" id="heroSpot"></div>
      <div class="hero-grain"></div>
      <div class="wrap hero-inner">
        <p class="eyebrow reveal-up">Web design studio · Brisbane</p>
        <h1 class="hero-title split">Bring your business <em>into the light.</em></h1>
        <p class="hero-lead reveal-up">Beautiful websites with online booking and payments, designed, built and set up for you. Live in a week, so you can get back to running your business.</p>
        <div class="hero-actions reveal-up">
          <a href="contact.html" class="btn magnetic">Start your project</a>
          <a href="packages.html" class="btn btn-ghost magnetic">See packages</a>
        </div>
      </div>
      <a href="#services" class="scroll-cue" aria-label="Scroll down"><span></span></a>
    </section>
{MARQUEE}

    <section class="section" id="services">
      <div class="wrap">
        <div class="section-head section-head-row">
          <div>
            <p class="eyebrow reveal-up">What we do</p>
            <h2 class="split">Everything your business needs <em>to be found and booked.</em></h2>
          </div>
          <a href="services.html" class="link-more reveal-up">All services <span>→</span></a>
        </div>{SERVICE_CARDS}
      </div>
    </section>

    <section class="section section-light">
      <div class="wrap work">
        <div class="work-copy">
          <p class="eyebrow eyebrow-dark reveal-up">Featured concept</p>
          <h2 class="split split-dark">A home grooming studio, <em>reimagined.</em></h2>
          <p class="reveal-up">A local pet groomer who relied on Instagram alone, given a seven-page site with online booking, deposits and local search set-up, built to turn followers into booked appointments.</p>
          <a href="work.html" class="link-more link-more-dark reveal-up">View the project <span>→</span></a>
        </div>{WORK_VISUAL}
      </div>
    </section>

    <section class="section" id="packages">
      <div class="wrap">
        <div class="section-head center">
          <p class="eyebrow reveal-up">Packages</p>
          <h2 class="split">Clear pricing. <em>No surprises.</em></h2>
          <p class="section-sub reveal-up">Fixed prices, so you know the total before we start. You own your website, domain and accounts.</p>
        </div>{PACKAGES}
        <p class="center reveal-up" style="margin-top:48px;"><a href="packages.html" class="link-more">Compare packages and FAQs <span>→</span></a></p>
      </div>
    </section>
{PROCESS}
""")

PAGES["services.html"] = ("Services | Lumière Digital Co",
 "Website design, online booking and payments, Google visibility and ongoing care for Brisbane small businesses.",
 False, page_hero("Services", "Everything you need <em>to be seen.</em>", "From the first impression to the booking confirmation, we design and set up every part of how customers find you and book you online.") + f"""

    <section class="section">
      <div class="wrap">{SERVICE_CARDS}
      </div>
    </section>

    <section class="section section-light">
      <div class="wrap detail-list">
        <div class="detail reveal-up">
          <p class="detail-num">01</p>
          <div><h2 class="split split-dark">Website design <em>and build</em></h2>
          <p>Your website is often the first thing a customer sees. We design it around your brand, write clear copy that explains what you do, and build it to load fast on any phone.</p>
          <ul class="tick-list"><li>Custom design, not a generic template</li><li>Mobile-first and fast-loading</li><li>Services, prices, gallery and contact pages</li><li>Copywriting help included</li></ul></div>
        </div>
        <div class="detail reveal-up">
          <p class="detail-num">02</p>
          <div><h2 class="split split-dark">Online booking <em>and payments</em></h2>
          <p>Stop losing evenings to booking messages. Customers choose a service and a time, pay a deposit and get reminders automatically.</p>
          <ul class="tick-list"><li>Square Appointments or Fresha, set up for you</li><li>Your services, prices and availability loaded in</li><li>Deposits, prepayment and gift cards</li><li>Automatic confirmations and reminders</li></ul></div>
        </div>
        <div class="detail reveal-up">
          <p class="detail-num">03</p>
          <div><h2 class="split split-dark">Found <em>on Google</em></h2>
          <p>A great website needs to be found. We build search-friendly from the start and make sure you show up when locals search for what you do.</p>
          <ul class="tick-list"><li>Search-ready page titles, descriptions and structure</li><li>Google Business Profile set-up</li><li>Google Maps and reviews linked to your site</li><li>Fast, secure hosting</li></ul></div>
        </div>
        <div class="detail reveal-up">
          <p class="detail-num">04</p>
          <div><h2 class="split split-dark">Care <em>after launch</em></h2>
          <p>Businesses change, and your website should keep up. With a care plan, updates are a quick message away.</p>
          <ul class="tick-list"><li>Price, menu and content updates</li><li>New photos and seasonal changes</li><li>Hosting and uptime checks</li><li>Priority support</li></ul></div>
        </div>
      </div>
    </section>
{PROCESS}
""")

PAGES["work.html"] = ("Work | Lumière Digital Co",
 "Website concepts and projects by Lumière Digital Co, including a seven-page site with online booking for a Brisbane pet grooming studio.",
 False, page_hero("Work", "Businesses, <em>brought into the light.</em>", "A look at how we turn a business that's hard to find online into one that's easy to find, trust and book.") + f"""

    <section class="section section-light">
      <div class="wrap work">
        <div class="work-copy">
          <p class="eyebrow eyebrow-dark reveal-up">Featured concept · Pet grooming</p>
          <h2 class="split split-dark">A home grooming studio, <em>reimagined.</em></h2>
          <p class="reveal-up">A cosy home grooming studio and daycare with a loyal local following, but no website. Bookings happened through Instagram messages, and new customers had no way to see prices or book after hours.</p>
          <ul class="tags reveal-up"><li>Website</li><li>Online booking</li><li>Payments</li><li>Local SEO</li></ul>
        </div>{WORK_VISUAL}
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="case-grid">
          <div class="case-col reveal-card"><p class="eyebrow">The challenge</p><p>Customers found the studio through Instagram but couldn't see services or prices, and every booking meant a back-and-forth of messages.</p></div>
          <div class="case-col reveal-card"><p class="eyebrow">What we built</p><p>A seven-page site with services and prices, a coat-care guide, an Instagram-style gallery, a full FAQ, and online booking with deposits and gift cards.</p></div>
          <div class="case-col reveal-card"><p class="eyebrow">The result</p><p>A professional home online that answers questions before they're asked and lets customers book any time, while the owner focuses on the grooming.</p></div>
        </div>
      </div>
    </section>

    <section class="section section-deep">
      <div class="wrap center">
        <p class="eyebrow reveal-up">Your business here</p>
        <h2 class="split">We're taking on <em>new projects.</em></h2>
        <p class="section-sub reveal-up">We're building our portfolio with Brisbane businesses now. Get in touch to be one of the first.</p>
        <p class="reveal-up" style="margin-top:36px;"><a href="contact.html" class="btn magnetic">Start your project</a></p>
      </div>
    </section>
""")

PAGES["packages.html"] = ("Packages and pricing | Lumière Digital Co",
 "Fixed-price website packages for Brisbane small businesses: Essential from $500, Bookings from $1,000, and care plans from $50 a month.",
 False, page_hero("Packages", "Clear pricing. <em>No surprises.</em>", "Fixed prices, so you know the total before we start. You own your website, domain and accounts, always.") + f"""

    <section class="section">
      <div class="wrap">{PACKAGES}
      </div>
    </section>

    <section class="section section-deep">
      <div class="wrap included-grid">
        <div><p class="eyebrow reveal-up">Every project includes</p><h2 class="split">The things that <em>matter.</em></h2></div>
        <ul class="tick-list tick-list-light reveal-up">
          <li>A fixed quote before we start</li>
          <li>You own your domain, hosting and accounts</li>
          <li>Two rounds of revisions</li>
          <li>Fast, secure hosting set up for you</li>
          <li>A walkthrough at launch</li>
          <li>Live in about a week once we have your content</li>
        </ul>
      </div>
    </section>

    <section class="section" id="faq">
      <div class="wrap faq-wrap">
        <div><p class="eyebrow reveal-up">Questions</p><h2 class="split">Good <em>to know</em></h2></div>
        <div class="faq">
          <details class="reveal-up"><summary>How long does a website take?</summary><p>Most sites are live within five to seven business days once we have your photos, prices and details.</p></details>
          <details class="reveal-up"><summary>How does payment work?</summary><p>A 50% deposit to begin, and the balance before your site goes live.</p></details>
          <details class="reveal-up"><summary>Do I own my website?</summary><p>Yes. Your domain, hosting, booking accounts and website files are all in your name. We're added as a collaborator so we can help.</p></details>
          <details class="reveal-up"><summary>Which booking systems do you use?</summary><p>Usually Square Appointments or Fresha, depending on your business. We set it up, add your services and connect it to your site.</p></details>
          <details class="reveal-up"><summary>Are there ongoing costs?</summary><p>Your domain costs a small yearly fee, and booking platforms charge their own fees. Hosting is usually free for sites like these. The care plan is optional.</p></details>
          <details class="reveal-up"><summary>What do I need to provide?</summary><p>Your logo if you have one, photos of your work, your services and prices, and your hours. We'll send a simple checklist.</p></details>
          <details class="reveal-up"><summary>What if I need changes later?</summary><p>Our care plan covers ongoing updates. Without one, changes are quoted per job before we start.</p></details>
        </div>
      </div>
    </section>
""")

PAGES["about.html"] = ("About | Lumière Digital Co",
 "Lumière means light. We help small businesses step out of the shadows online, so customers can find them, trust them and book them.",
 False, page_hero("About", "Great businesses <em>deserve to be seen.</em>", "Lumière exists to give small businesses the kind of online presence that used to be reserved for big brands, without the big-brand price or the hassle.") + """

    <section class="section meaning">
      <div class="meaning-glow" id="meaningGlow"></div>
      <div class="wrap meaning-inner">
        <p class="eyebrow reveal-up">The name</p>
        <h2 class="meaning-word split"><em>lumière</em></h2>
        <p class="meaning-def reveal-up"><span>noun · French</span> light</p>
        <p class="meaning-copy reveal-up">Light is what makes things visible. Without it, even the best work goes unseen. The name also nods to the Lumière brothers, who pioneered cinema in 1895 and showed the world what a single beam of light could do.</p>
      </div>
    </section>

    <section class="section section-light">
      <div class="wrap purpose">
        <div>
          <p class="eyebrow eyebrow-dark reveal-up">Why we exist</p>
          <h2 class="split split-dark">Too many great businesses <em>stay in the shadows.</em></h2>
        </div>
        <div class="purpose-copy">
          <p class="reveal-up">Every suburb is full of brilliant small businesses: the groomer with a waitlist, the café locals swear by, the tradie who always turns up. Yet many of them are almost invisible online, relying on word of mouth, a social media page or a website that hasn't been touched in years.</p>
          <p class="reveal-up">Meanwhile, customers are searching, comparing and booking online, often late at night, and they choose the business they can find and book easily.</p>
          <p class="reveal-up">Lumière closes that gap. We give small businesses a professional website and online booking that work around the clock, so owners can spend less time on admin and more time doing what they love.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head center">
          <p class="eyebrow reveal-up">What we believe</p>
          <h2 class="split">Simple, honest <em>and done properly.</em></h2>
        </div>
        <div class="values">
          <article class="value reveal-card"><span class="service-num">01</span><h3>Professional shouldn't mean expensive</h3><p>Small businesses deserve a website that looks as good as their work, at a price that makes sense.</p></article>
          <article class="value reveal-card"><span class="service-num">02</span><h3>Done for you, from start to finish</h3><p>Business owners are busy. We handle the design, the tech and the set-up, and explain it all in plain English.</p></article>
          <article class="value reveal-card"><span class="service-num">03</span><h3>You own everything</h3><p>Your domain, your accounts, your website. No lock-in contracts and nothing held hostage.</p></article>
        </div>
      </div>
    </section>

    <section class="section section-deep">
      <div class="wrap who">
        <div><p class="eyebrow reveal-up">Who we work with</p><h2 class="split">Local businesses <em>with something to show.</em></h2></div>
        <ul class="who-list reveal-up">
          <li>Pet groomers and daycares</li><li>Cafés and restaurants</li><li>Beauty and hair salons</li><li>Wellness practitioners</li><li>Trades and home services</li><li>Studios and boutiques</li>
        </ul>
      </div>
    </section>
""")

PAGES["contact.html"] = ("Contact | Lumière Digital Co",
 "Start your website project with Lumière Digital Co. Tell us about your business and we'll be in touch within one business day.",
 False, page_hero("Contact", "Let's bring your business <em>into the light.</em>", "Tell us a little about your business and we'll be in touch within one business day.") + """

    <section class="section contact">
      <div class="wrap contact-inner">
        <div class="contact-copy">
          <p class="eyebrow reveal-up">What happens next</p>
          <ol class="next-steps reveal-up">
            <li><strong>We reply within one business day</strong> to book a quick, no-obligation chat.</li>
            <li><strong>You get a fixed quote,</strong> so you know the total before anything starts.</li>
            <li><strong>We get to work,</strong> and your site is live in about a week once we have your content.</li>
          </ol>
          <p class="contact-email reveal-up"><a href="mailto:hello@lumieredigitalco.com">hello@lumieredigitalco.com</a></p>
        </div>
        <!-- Enquiries are saved to the Lumière Supabase database and appear in the portal -->
        <form class="contact-form reveal-up" id="contactForm" novalidate
              data-endpoint="https://uhopcqdltsncefslslue.supabase.co/rest/v1/enquiries"
              data-key="sb_publishable_B6H15I5XwG2hrQM3sXc_sw_BhzSXz9h">
          <div class="hp" aria-hidden="true"><label for="f-website">Leave this empty</label><input id="f-website" name="website" tabindex="-1" autocomplete="off"></div>
          <div class="field"><input id="f-name" name="name" required placeholder=" "><label for="f-name">Your name</label></div>
          <div class="field"><input id="f-biz" name="business" placeholder=" "><label for="f-biz">Business name</label></div>
          <div class="field"><input id="f-email" name="email" type="email" required placeholder=" "><label for="f-email">Email</label></div>
          <div class="field"><input id="f-phone" name="phone" type="tel" placeholder=" "><label for="f-phone">Phone</label></div>
          <div class="field field-full">
            <select id="f-pkg" name="package"><option>Not sure yet</option><option>Essential</option><option>Bookings</option><option>Care plan</option><option>Something custom</option></select>
            <label for="f-pkg" class="label-static">Interested in</label>
          </div>
          <div class="field field-full"><textarea id="f-msg" name="message" rows="4" placeholder=" "></textarea><label for="f-msg">Tell us about your business</label></div>
          <p class="form-consent field-full">By sending this form, you agree to us using your details to respond to your enquiry, as set out in our <a href="privacy.html">Privacy Policy</a>.</p>
          <button class="btn magnetic" type="submit">Send enquiry</button>
          <p class="form-note" id="formNote" role="status"></p>
        </form>
      </div>
    </section>
""")

def legal_page(title, intro, body):
    return page_hero("Legal", title, intro).replace('class="hero hero-page"','class="hero hero-page hero-legal"') + f"""

    <section class="section">
      <div class="wrap legal">
{body}
      </div>
    </section>
"""

PAGES["privacy.html"] = ("Privacy Policy | Lumière Digital Co",
 "How Lumière Digital Co collects, uses, stores and protects your personal information.",
 False, legal_page("Privacy <em>Policy</em>", "Last updated 28 October 2026", """
        <p>Lumière Digital Co is a business name of Aurella Group Pty Ltd (ABN 70 649 742 423) ("we", "us", "our"). We respect your privacy. This policy explains how we collect, use, store and disclose personal information through our website, lumieredigitalco.com, and in the course of our business. We handle personal information in line with the Australian Privacy Principles in the <em>Privacy Act 1988</em> (Cth).</p>

        <h2>1. What we collect</h2>
        <p>We only collect personal information that we need to respond to you and provide our services. This may include:</p>
        <ul>
          <li>your name, business name, email address and phone number</li>
          <li>details you share about your business and project</li>
          <li>information needed to deliver your project, such as content, images and account access you provide</li>
          <li>billing details needed to send invoices (we don't store card details; payments are processed by our payment provider)</li>
        </ul>

        <h2>2. How we collect it</h2>
        <p>We collect personal information directly from you, when you fill in our contact form, email or call us, or work with us on a project. We don't buy personal information from third parties.</p>

        <h2>3. How we use it</h2>
        <p>We use your personal information to:</p>
        <ul>
          <li>respond to your enquiry and provide quotes</li>
          <li>deliver, support and maintain your website and related services</li>
          <li>send invoices and manage our business records</li>
          <li>meet our legal obligations</li>
        </ul>
        <p>We won't send you marketing emails unless you've agreed to receive them, and you can opt out at any time.</p>

        <h2>4. Who we share it with</h2>
        <p>We don't sell or rent your personal information. We share it only with service providers who help us run our business, and only as needed. These include:</p>
        <ul>
          <li>our website hosting provider</li>
          <li>our database provider (Supabase), which securely stores contact form submissions</li>
          <li>our email, accounting and payment providers</li>
          <li>professional advisers, such as our accountant, where necessary</li>
        </ul>
        <p>We may also disclose information where required or authorised by law.</p>

        <h2>5. Overseas disclosure</h2>
        <p>Some of our service providers store data on servers outside Australia, including in the United States. Where this happens, we take reasonable steps to make sure those providers protect your information in a way that is consistent with Australian privacy law.</p>

        <h2>6. Cookies and similar technologies</h2>
        <p>Our website does not use advertising or tracking cookies. We use your browser's temporary session storage only to remember that you've already seen our opening animation, so it doesn't replay on every page. This information stays in your browser and is cleared when you close it.</p>
        <p>Our website loads fonts from Google Fonts and animation code from cdnjs (Cloudflare). When your browser requests these files, those providers receive standard technical information such as your IP address. Please see their privacy policies for details.</p>
        <p>If we introduce analytics in the future, we'll update this policy first and favour privacy-friendly tools that don't use tracking cookies.</p>

        <h2>7. Storage and security</h2>
        <p>We take reasonable steps to protect personal information from misuse, interference, loss, and unauthorised access, change or disclosure. This includes using reputable providers, secure passwords and two-factor authentication where available. When information is no longer needed, we delete or de-identify it.</p>

        <h2>8. Client website data</h2>
        <p>When we build or maintain a website for a client, that client is responsible for the personal information collected through their own website and booking systems. We access it only as needed to provide our services.</p>

        <h2>9. Accessing or correcting your information</h2>
        <p>You can ask to see the personal information we hold about you, or ask us to correct it, by emailing us. We'll respond within a reasonable time, usually within 30 days.</p>

        <h2>10. Links to other websites</h2>
        <p>Our website may link to other websites. We're not responsible for their content or privacy practices.</p>

        <h2>11. Complaints</h2>
        <p>If you have a concern about how we've handled your personal information, please contact us first and we'll do our best to resolve it. If you're not satisfied with our response, you can contact the Office of the Australian Information Commissioner at <a href="https://www.oaic.gov.au" target="_blank" rel="noopener">oaic.gov.au</a>.</p>

        <h2>12. Changes to this policy</h2>
        <p>We may update this policy from time to time. The latest version will always be on this page, with the date it was last updated.</p>

        <h2>13. Contact us</h2>
        <p>Lumière Digital Co<br>Aurella Group Pty Ltd · ABN 70 649 742 423<br>Brisbane, Queensland<br><a href="mailto:hello@lumieredigitalco.com">hello@lumieredigitalco.com</a></p>
"""))

PAGES["terms.html"] = ("Terms of Website Use | Lumière Digital Co",
 "The terms that apply when you use the Lumière Digital Co website.",
 False, legal_page("Terms of <em>Website Use</em>", "Last updated 28 October 2026", """
        <p>These terms apply to your use of lumieredigitalco.com (the "website"), operated by Aurella Group Pty Ltd (ABN 70 649 742 423), trading as Lumière Digital Co ("we", "us", "our"). By using the website, you agree to these terms. If you don't agree, please don't use the website.</p>

        <h2>1. About this website</h2>
        <p>This website provides general information about our web design, booking set-up and website care services. It is not an offer to provide services on particular terms.</p>

        <h2>2. Prices and quotes</h2>
        <p>Prices on this website are shown as "from" prices, are in Australian dollars and are a guide only. The final price for your project will be set out in a written quote. Our services are provided under a separate written agreement, which applies instead of these terms to any work we do for you.</p>

        <h2>3. Intellectual property</h2>
        <p>Unless otherwise stated, the content of this website, including text, design, graphics, logos, animations and code, is owned by or licensed to us and protected by copyright and other laws. You may view and share our pages for personal, non-commercial use, but you may not copy, reproduce or reuse our content, branding or design without our written permission.</p>
        <p>Some images on this website are used under licence from third parties, and some projects shown are concepts created to demonstrate our work.</p>

        <h2>4. Acceptable use</h2>
        <p>You must not use this website in a way that is unlawful, harmful or disruptive, or that interferes with its operation or security, including by attempting to gain unauthorised access or by submitting spam or malicious content through our forms.</p>

        <h2>5. Accuracy of information</h2>
        <p>We take care to keep the website accurate and up to date, but we don't guarantee that all information is complete, current or free from errors. Information on the website is general in nature and not professional advice for your particular situation.</p>

        <h2>6. Links to other websites</h2>
        <p>The website may link to third-party websites. These links are provided for convenience, and we're not responsible for the content, products or practices of those websites.</p>

        <h2>7. Liability</h2>
        <p>Nothing in these terms excludes, restricts or modifies any rights you have under the Australian Consumer Law that cannot be excluded. To the extent permitted by law, we are not liable for any loss or damage arising from your use of, or inability to use, the website, including loss caused by viruses, interruptions or reliance on information on the website.</p>

        <h2>8. Privacy</h2>
        <p>Our <a href="privacy.html">Privacy Policy</a> explains how we handle personal information collected through the website.</p>

        <h2>9. Changes</h2>
        <p>We may update these terms at any time by publishing a new version on this page. Your continued use of the website means you accept the updated terms.</p>

        <h2>10. Governing law</h2>
        <p>These terms are governed by the laws of Queensland, Australia, and you agree to the non-exclusive jurisdiction of the courts of Queensland.</p>

        <h2>11. Contact us</h2>
        <p>Lumière Digital Co<br>Aurella Group Pty Ltd · ABN 70 649 742 423<br>Brisbane, Queensland<br><a href="mailto:hello@lumieredigitalco.com">hello@lumieredigitalco.com</a></p>
"""))

for path, (title, desc, intro, body) in PAGES.items():
    cta = FOOTER if path != "contact.html" else FOOTER.replace(FOOTER[FOOTER.index('  <section class="cta-band">'):FOOTER.index('  <footer')], "")
    html = head(title, desc, path) + f'\n<body class="{"is-loading" if intro else ""}">\n' + (INTRO if intro else "") + header(path) + '\n  <main id="top">' + body + "\n  </main>\n" + cta
    (ROOT / path).write_text(html)
    print("wrote", path)

(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}/{'' if p == 'index.html' else p}</loc></url>\n" for p in PAGES) + "</urlset>\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
