// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/app/css/index.css',
    '/static/app/image/carrusel/Como.jpg',
    '/static/app/image/carrusel/wms.jpg',
    '/static/app/image/carrusel/gestión-de-inventario-1200x565.jpg',
    '/static/app/image/carrusel/tms.jpg',
    '/static/app/image/estrategias.png',

];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
        .then(cache => {
            return cache.addAll(filesToCache);
        })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                .filter(cacheName => (cacheName !== staticCacheName))
                .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener('fetch', function(event) {
    event.respondWith(

        fetch(event.request)
        .then(function(response) {
            return caches.open(staticCacheName)
                .then(function(c) {
                    c.put(event.request.url, result.clone())
                    return result;
                })

        })
        .catch(function(e) {
            return caches.match(event.request)
        })



    );
});