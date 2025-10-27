document.addEventListener('DOMContentLoaded', function() {
    const videoPlayers = document.querySelectorAll('.video-player');
    
    videoPlayers.forEach(video => {
        const overlay = video.parentElement.querySelector('.video-overlay');
        const playButton = overlay.querySelector('.play-button');
        
        // Клик по оверлею - воспроизведение
        overlay.addEventListener('click', function() {
            video.play();
            overlay.classList.add('hidden');
        });
        
        // Клик по кнопке play
        playButton.addEventListener('click', function(e) {
            e.stopPropagation();
            video.play();
            overlay.classList.add('hidden');
        });
        
        // При паузе показываем оверлей
        video.addEventListener('pause', function() {
            overlay.classList.remove('hidden');
        });
        
        // При окончании видео показываем оверлей
        video.addEventListener('ended', function() {
            overlay.classList.remove('hidden');
        });
    });
});