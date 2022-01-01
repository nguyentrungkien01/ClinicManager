let doctor = [{
        majorClass: 'Cardiologist Pediatricians',
        star: '4.5',
        avatar: 'https://res.cloudinary.com/ouproject/image/upload/v1639921916/img/team/team1_irfyhk.jpg',
        name: 'Dr. Johnson',
        majorName: 'Bác sỹ tim mạch',
        phone: '+4733378901'
    },
    {
        majorClass: 'Surgeon Gynecologist',
        star: '4.5',
        avatar: 'https://res.cloudinary.com/ouproject/image/upload/v1639921916/img/team/team2_ylquip.jpg',
        name: 'Dr. Nam',
        majorName: 'Bác sỹ phẫu thuật',
        phone: '+4733378901'
    },
    {
        majorClass: 'Dentist',
        star: '4.5',
        avatar: 'https://res.cloudinary.com/ouproject/image/upload/v1639921918/img/team/team3_ldjnqk.jpg',
        name: 'Dr. Jorz Maxwell',
        majorName: 'Bác sỹ nha khoa',
        phone: '+4733378901'
    },
    {
        majorClass: 'Gynecologist Surgeon',
        star: '4.5',
        avatar: 'https://res.cloudinary.com/ouproject/image/upload/v1639921916/img/team/team4_cfcdxa.jpg',
        name: 'Dr. Nilla Roy',
        majorName: 'Bác sỹ phụ khoa',
        phone: '+4733378901'
    },
    {
        majorClass: 'Pediatricians Cardiologist',
        star: '4.5',
        avatar: 'https://res.cloudinary.com/ouproject/image/upload/v1639921916/img/team/team5_flziuj.jpg',
        name: 'Dr. Adam Jani',
        majorName: 'Bác sỹ nha khoa',
        phone: '+4733378901'
    },
    {
        majorClass: 'Cardiologist Gynecologist',
        star: '4.5',
        avatar: 'https://res.cloudinary.com/ouproject/image/upload/v1639921916/img/team/team6_hofjmk.jpg',
        name: 'Dr. Nikki Bella',
        majorName: 'Bác sỹ phụ khoa',
        phone: '+4733378901'
    },
    {
        majorClass: 'Surgeon Gynecologist',
        star: '4.5',
        avatar: 'https://res.cloudinary.com/ouproject/image/upload/v1639921916/img/team/team7_gokkex.jpg',
        name: 'Dr. Sanju Samson',
        majorName: 'Bác sỹ phụ khoa',
        phone: '+4733378901'
    },
    {
        majorClass: 'Dentist',
        star: '4.5',
        avatar: 'https://res.cloudinary.com/ouproject/image/upload/v1639921918/img/team/team8_snhoeh.jpg',
        name: 'Dr. Charus Dolly',
        majorName: 'Bác sỹ nha khoa',
        phone: '+4733378901'
    }
]

let doctor_list = document.querySelector('#doctor-list')
renderMusic = (item) => {
    item.forEach(e => {
        let prod =
            `
        <div class="hc-team-box col-lg-4 col-md-6 col-sm-12 ${e.majorClass}">
            <span class="hc-dr-rating"><i class="fas fa-star"></i>  ${e.star}</span>
        <div class="hc-team-img">
            <img src="${e.avatar}" alt="team" />
        </div>
            <h1 class="hc-team-name">${e.name}</h1>
            <h2 class="hc-team-designation">${e.majorName}</h2>
            <p>${e.majorClass}</p>
        <ul class="hc-team-social">
            <li>
                <a href="javacript:;"><i class="fab fa-facebook-f"></i></a>
            </li>
            <li>
                <a href="javacript:;"><i class="fab fa-twitter"></i></a>
            </li>
            <li>
                <a href="tel:${e.phone}"><i class="fas fa-phone-alt"></i></a>
            </li>
        </ul>
    </div>
`
        doctor_list.insertAdjacentHTML("beforeend", prod)
    })
}
renderMusic(doctor);