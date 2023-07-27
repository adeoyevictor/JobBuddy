let jobs_list = []
// let modal_job = null

document.addEventListener('DOMContentLoaded', () => {
    let active = localStorage.getItem('active') ? JSON.parse(localStorage.getItem('active')) : true
    const switch_box = document.querySelector('.switch > [type="checkbox"]')
    if (active) {
        switch_box.checked = false
    }
    else {
        switch_box.checked = true
    }

    const board = document.querySelector('.board')
    const switch_icon = document.querySelector('.switch > .slide')
    const archived = document.querySelector('.archived')
    const active_text = document.querySelector('.active')
    archived.style.fontWeight = active ? 'normal' : 'bold'
    active_text.style.fontWeight = active ? 'bold' : 'normal'

    switch_icon.addEventListener('click', (event) => {
        active = !active
        localStorage.setItem('active', String(active))
        archived.style.fontWeight = active ? 'normal' : 'bold'
        active_text.style.fontWeight = active ? 'bold' : 'normal'

        displayJobs(false, active)
    })

    const switch_container = document.querySelector('.switch-container')
    const loader = document.querySelector('.loader-container')
    board.style.display = 'none'
    switch_container.style.display = 'none'


    fetch('/jobs')
        .then(res => res.json())
        .then(jobs => {
            jobs_list = jobs_list.concat(jobs)
            displayJobs(true, active)
            // remove loader
            board.style.display = 'grid'
            switch_container.style.display = 'grid'
            loader.style.display = 'none'
        })

    const sortableLists = document.querySelectorAll('.sortable-list');

    sortableLists.forEach(list => {
        new Sortable(list, {
            group: 'kanban',
            animation: 150,
            onEnd: function (evt) {
                fetch(`/jobs/${Number(evt.item.dataset.id)}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        stage: evt.to.dataset.stage
                    })
                }).then(() => {
                    console.log('Updated Stage');
                })
            }

        });
    });


})

function displayJobs(onload, active) {
    const NOT_APPLIED = jobs_list.filter(job => job.stage === 'NOT_APPLIED' && job.archived === !active)
    const APPLIED = jobs_list.filter(job => job.stage === 'APPLIED' && job.archived === !active)
    const FIRST_INTERVIEW = jobs_list.filter(job => job.stage === 'FIRST_INTERVIEW' && job.archived === !active)
    const FOLLOW_UP_INTERVIEWS = jobs_list.filter(job => job.stage === 'FOLLOW_UP_INTERVIEWS' && job.archived === !active)
    const OFFER = jobs_list.filter(job => job.stage === 'OFFER' && job.archived === !active)
    document.querySelector('.not-applied').textContent = NOT_APPLIED.length
    document.querySelector('.applied').textContent = APPLIED.length
    document.querySelector('.first-interview').textContent = FIRST_INTERVIEW.length
    document.querySelector('.follow-up-interviews').textContent = FOLLOW_UP_INTERVIEWS.length
    document.querySelector('.offer').textContent = OFFER.length
    // add cards
    const card1 = document.querySelector('.card1')
    const card2 = document.querySelector('.card2')
    const card3 = document.querySelector('.card3')
    const card4 = document.querySelector('.card4')
    const card5 = document.querySelector('.card5')

    if (!onload) {
        card1.innerHTML = ''
        card2.innerHTML = ''
        card3.innerHTML = ''
        card4.innerHTML = ''
        card5.innerHTML = ''
    }

    NOT_APPLIED.forEach(job => {
        card1.appendChild(createDiv(job.color, job.title, job.company, job.location, active, job.id))
    })
    APPLIED.forEach(job => {
        card2.appendChild(createDiv(job.color, job.title, job.company, job.location, active, job.id))
    })
    FIRST_INTERVIEW.forEach(job => {
        card3.appendChild(createDiv(job.color, job.title, job.company, job.location, active, job.id))
    })
    FOLLOW_UP_INTERVIEWS.forEach(job => {
        card4.appendChild(createDiv(job.color, job.title, job.company, job.location, active, job.id))
    })
    OFFER.forEach(job => {
        card5.appendChild(createDiv(job.color, job.title, job.company, job.location, active, job.id))
    })
}


function createDiv(color, title, company, location, active, id) {
    const div = document.createElement('div')
    div.className = 'item'
    div.setAttribute('data-id', id)
    div.style.borderRightColor = color
    const content = `<h4>${title}</h4>
                <p>${company}</p>
                <span>${location}</span><div class="icons">
${active ? `<i class="bi bi-archive" id="archive" title="Archive"></i>` : `<i class="bi bi-trash" id="delete" title="Delete"></i>`}
</div>
`
    div.innerHTML = content
    div.addEventListener('click', (event) => {
        if (event.target.id === 'archive') {
            archiveJob(id, event.target.parentElement.parentElement)
        }
        else if (event.target.id === 'delete') {
            deleteJob(id, event.target.parentElement.parentElement)
        }
        else {
            viewJob(id)
        }
    })


    return div
}

function archiveJob(id, parent) {
    fetch(`/jobs/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: true
        })
    }).then(() => {
        jobs_list = jobs_list.map(job => job.id === id ? {
            ...job,
            archived: true
        } : job)
        parent.remove()
    })
}
function deleteJob(id, parent) {
    fetch(`/jobs/${id}`, {
        method: 'DELETE'
    }).then(() => {
        jobs_list = jobs_list.filter(job => job.id !== id)
        parent.remove()
    })
}
function viewJob(id) {
    window.location.href = `/job/${id}`
}
