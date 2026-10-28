# Lumière Digital Co website

Static site with no build step. Deploy the folder as-is to Vercel, Cloudflare Pages or Netlify (output directory: root).

- `index.html`: all page content and copy
- `assets/css/style.css`: colours and fonts at the top (`:root`)
- `assets/js/main.js`: animations (GSAP and ScrollTrigger, loaded from cdnjs)
- `assets/img/`: logos and icons. Favicons sit in the root folder.

The light-bulb intro plays once per browser session and has a "Skip intro" button. It's skipped automatically for visitors who have reduced motion turned on in their device settings.

## Intro video
`assets/video/bulb.mp4` and `bulb.webm` are a 4.3-second cut of the Videezy clip "Light Bulb 43", colour-graded to black. Check the clip's licence for commercial use, and add attribution if the licence requires it.

## Before launch
- Contact form: saves enquiries to the Lumière Supabase project (table `enquiries`), shown in the portal.
- ABN is set to Aurella Group Pty Ltd (70 649 742 423).
- Replace the Unsplash concept images in the Work section with real client work once you have permission to show it.
