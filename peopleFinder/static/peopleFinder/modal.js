function openPersonModal(id) {
    var modal = document.getElementById('person-modal-container');
    modal.style.display = 'block';
    var modalContent = document.getElementById('person-modal-content');
    axios.get('/people-finder/' + id).then(function(results) {
        modalContent.innerHTML = results.data;
    }).catch(function(error) {
        alert(error.message);
    });
}

function closePersonModal(id) {
    var modal = document.getElementById('person-modal-container');
    modal.style.display = 'none';
    var modalContent = document.getElementById('person-modal-content');
    modalContent.innerHTML = '<p>Loading...</p>';
}
