# FreshTrack

Web de **FreshTrack**, la app iOS para controlar caducidades de alimentos con etiquetas NFC.

- Web: https://freshtrack.softapp.tech/ · [English](https://freshtrack.softapp.tech/en/)
- App Store: https://apps.apple.com/app/id6791699550
- [Privacidad](https://freshtrack.softapp.tech/privacidad.html)

Sitio estático servido por GitHub Pages desde la raíz del repositorio.

## Despliegue

**No hay build ni Actions: cada `git push` a `master` publica el árbol completo tal cual**, en
menos de un minuto. No existe forma de "commitear sin publicar" en `master` — todo lo que hay ahí
está en producción.

Si una función no debe salir todavía (por ejemplo, algo de una versión de la app que aún no ha
aprobado App Review), va a **otra rama** (`git checkout -b nombre-feature`, commit, `git push -u
origin nombre-feature`) y no se toca `master` hasta que toque publicarla. GitHub Pages ignora
cualquier rama que no sea `master`.

Para comprobar qué commit está sirviendo Pages ahora mismo y si ya ha terminado de construir:

```bash
gh api repos/jmhdevelop/freshtrack-web/pages/builds/latest
```

## Otras apps

- [Dibus](https://dibus.softapp.tech/) — colorear para niños
- [DevToolbox](https://devtoolbox.softapp.tech/) — limpieza y monitorización para Mac

Todas las apps de la casa, en <https://softapp.tech>.
