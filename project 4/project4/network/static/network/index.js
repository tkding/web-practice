document.addEventListener('DOMContentLoaded', function() {
    // edit post
    const editPostButtons = document.querySelectorAll('.edit-post-btn');

    editPostButtons.forEach(editButton => {
        editButton.addEventListener('click', () => {
            console.log('edit button clicked');
            const postId = editButton.getAttribute('data-post-id');
            const editForm = document.querySelector(`.edit-post-form[data-post-id="${postId}"]`);
            const editTextarea = editForm.querySelector('.edit-post-textarea');

            // Toggle the 'hidden' attribute of the edit form
            if (editForm.hasAttribute('hidden')) {
                // Show the edit form and populate the textarea with original content
                editForm.removeAttribute('hidden');
                editTextarea.value = editForm.getAttribute('data-original-content');
            } else {
                // Hide the edit form and reset the textarea
                editForm.setAttribute('hidden', 'true');
                editTextarea.value = ''; // Reset the textarea content
            }
        });
    });

    const savePostButtons = document.querySelectorAll('.save-post-btn');

    savePostButtons.forEach(saveButton => {
        saveButton.addEventListener('click', () => {
            console.log('save button clicked');
            const postId = saveButton.getAttribute('data-post-id');
            const editedContent = document.querySelector(`.edit-post-form[data-post-id="${postId}"] .edit-post-textarea`).value;

            fetch(`/edit_post/${postId}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ content: editedContent }), // update the content
            })
            .then(response => response.json()) // convert to json
            .then(data => {
                if (data.success) {
                    // Update the post content
                    const postContent = document.querySelector(`.post-content[data-post-id="${postId}"]`);
                    postContent.textContent = editedContent;

                    // Hide the edit form
                    const editForm = document.querySelector(`.edit-post-form[data-post-id="${postId}"]`);
                    editForm.setAttribute('data-original-content', editedContent);
                    editForm.setAttribute('hidden', 'true');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    // function to get CSRF token from cookie
    function getCookie(name){
        let cookieValue = null;
        if(document.cookie && document.cookie !== ''){
            const cookies = document.cookie.split(';');
            for(let i = 0; i < cookies.length; i++){
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if(cookie.substring(0, name.length + 1) === (name + '=')){
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // like/unlike post
    const likeButtons = document.querySelectorAll('.like-btn');

    likeButtons.forEach(likeButton => {
        likeButton.addEventListener('click', () => {
            console.log('like button clicked');
            const postId = likeButton.getAttribute('data-post-id');
            const likeCount = document.querySelector(`.like-count[data-post-id="${postId}"]`);

            fetch(`/like_post/${postId}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json()) // convert to json
            .then(data => {
                if (data.success) {
                    // Update the like count
                    likeCount.textContent = data.like_count;

                    // Toggle the like/unlike button
                    if (data.liked) {
                        likeButton.classList.add('liked');
                    } else {
                        likeButton.classList.remove('liked');
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});

