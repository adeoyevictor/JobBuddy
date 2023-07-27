document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.job-form')


    form.addEventListener('submit', (event) => {
        event.preventDefault()
        const title = document.querySelector('#title').value
        const company = document.querySelector('#company').value
        const location = document.querySelector('#location').value
        const url = document.querySelector('#url').value
        const description = document.querySelector('#description').value
        const level = document.querySelector('#level').value
        const mode = document.querySelector('#mode').value
        const stage = document.querySelector('#stage').value
        const posting_date = document.querySelector('#posting_date').value
        const colors = document.getElementsByName('color')
        let color = ''

        for (let i = 0, n = colors.length; i < n; i++) {
            if (colors[i].checked) {
                color = colors[i].value
                break
            }
        }
        fetch('/add', {
            method: 'POST',
            body: JSON.stringify({
                title,
                company,
                location,
                url,
                description,
                level,
                mode,
                stage,
                posting_date,
                color
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                window.location.href = '/'
            })
            .catch(error => {
                console.log(error);
            })

    })
})

