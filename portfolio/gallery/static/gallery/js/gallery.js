// Функция для инициализации слайдера
function initSlider(sliderMainId) {
    // Находим основной контейнер слайдера
    const sliderMain = document.getElementById(sliderMainId);
    const sliderContainer = sliderMain.closest('.gallery-slider');
    
    // Получаем все элементы слайдера
    const images = sliderMain.querySelectorAll('img');
    const thumbnails = sliderContainer.querySelectorAll('.slider-thumbnail');
    const prevBtn = sliderContainer.querySelector('.prev-btn');
    const nextBtn = sliderContainer.querySelector('.next-btn');
    
    let currentIndex = 0;
    
    // Показываем текущее изображение
    function showImage(index) {
        // Скрываем все изображения
        images.forEach(img => img.classList.remove('active'));
        // Убираем активный класс со всех миниатюр
        thumbnails.forEach(thumb => thumb.classList.remove('active'));
        
        // Показываем текущее изображение
        images[index].classList.add('active');
        // Активируем соответствующую миниатюру
        thumbnails[index].classList.add('active');
        currentIndex = index;
    }
    
    // Переход к следующему изображению
    function nextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    }
    
    // Переход к предыдущему изображению
    function prevImage() {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        showImage(currentIndex);
    }
    
    // Добавляем обработчики событий
    nextBtn.addEventListener('click', nextImage);
    prevBtn.addEventListener('click', prevImage);
    
    // Добавляем обработчики кликов на миниатюры
    thumbnails.forEach((thumb, index) => {
        thumb.addEventListener('click', () => showImage(index));
    });
    
    // Инициализируем первое изображение
    if (images.length > 0) {
        showImage(0);
    }
}

// Инициализация всех слайдеров после загрузки DOM
document.addEventListener('DOMContentLoaded', function() {
    // Находим все слайдеры на странице
    const sliders = document.querySelectorAll('.gallery-slider');
    
    // Инициализируем каждый слайдер
    sliders.forEach((slider, index) => {
        const sliderMain = slider.querySelector('.slider-main');
        if (sliderMain) {
            // Если у slider-main нет id, создаем его
            if (!sliderMain.id) {
                sliderMain.id = `slider-${index}`;
            }
            initSlider(sliderMain.id);
        }
    });
});