document.addEventListener('DOMContentLoaded', function() {
    const selectWrappers = document.querySelectorAll('.select-wrapper');
    
    selectWrappers.forEach(wrapper => {
        const nativeSelect = wrapper.querySelector('select');
        const customSelect = wrapper.querySelector('.select-items');
        const selectArrow = wrapper.querySelector('.select-arrow');
        const options = wrapper.querySelectorAll('.select-option');
        
        // Создаем видимый элемент для отображения выбранного значения
        const selectedDisplay = document.createElement('div');
        selectedDisplay.className = 'select-selected';
        selectedDisplay.innerHTML = `
            <span class="selected-value">
                ${nativeSelect.options[nativeSelect.selectedIndex].text}
            </span>
        `;
        wrapper.insertBefore(selectedDisplay, nativeSelect.nextSibling);
        
        // Обработчик клика по "стрелке"
        selectArrow.addEventListener('click', function(e) {
            e.stopPropagation();
            customSelect.style.display = customSelect.style.display === 'block' ? 'none' : 'block';
            selectArrow.classList.toggle('active');
        });
        
        // Обработчики для вариантов выбора
        options.forEach(option => {
            option.addEventListener('click', function() {
                const value = this.getAttribute('data-value');
                nativeSelect.value = value;
                wrapper.querySelector('.selected-value').textContent = this.textContent;
                
                // Закрываем выпадающий список
                customSelect.style.display = 'none';
                selectArrow.classList.remove('active');
                
                // Обновляем стиль выбранного варианта
                options.forEach(opt => opt.classList.remove('selected'));
                this.classList.add('selected');
            });
        });
        
        // Закрытие при клике вне элемента
        document.addEventListener('click', function(e) {
            if (!wrapper.contains(e.target)) {
                customSelect.style.display = 'none';
                selectArrow.classList.remove('active');
            }
        });
        
        // Синхронизация при изменении нативного select
        nativeSelect.addEventListener('change', function() {
            wrapper.querySelector('.selected-value').textContent = this.options[this.selectedIndex].text;
        });
    });
});