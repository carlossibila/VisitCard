// Platform-specific map routing
function openMaps() {
    const address = "Rua Quadrangular 3622, Primo Meneghetti, Franca, SP, 14403-220";
    const encodedAddress = encodeURIComponent(address);
    const userAgent = navigator.userAgent || navigator.vendor || window.opera;

    let mapUrl;

    // iOS - Open Apple Maps (using HTTP scheme which works in Safari and triggers app)
    if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
        mapUrl = `https://maps.apple.com/?q=${encodedAddress}`;
    }
    // Android - Open Google Maps app via intent
    else if (/android/i.test(userAgent)) {
        mapUrl = `https://www.google.com/maps/search/?api=1&query=${encodedAddress}`;
    }
    // Desktop/Other - Open Google Maps web
    else {
        mapUrl = `https://www.google.com/maps/search/?api=1&query=${encodedAddress}`;
    }

    window.location.href = mapUrl;
}
