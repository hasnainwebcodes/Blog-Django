var script = document.createElement('script');
script.type= 'text/javascript';
script.src="https://cdn.tiny.cloud/1/nf4bil7wg5pxbgmqb4w3ddhdsjy866upxqanp2wwl1dv0gkv/tinymce/6/tinymce.min.js"
document.head.appendChild(script);
script.onload= function(){
tinymce.init({
            selector: '#id_content',
            height: 600,

            /* 🔥 EXACT PHOTO-LIKE FEATURES */
            menubar: 'file edit view insert format tools table help',

            plugins: [
                'advlist', 'autolink', 'lists', 'link', 'image',
                'charmap', 'preview', 'anchor',
                'searchreplace', 'visualblocks', 'code',
                'fullscreen', 'insertdatetime', 'media',
                'table', 'help', 'wordcount'
            ],

            toolbar:
                'undo redo | formatselect | ' +
                'bold italic underline strikethrough | forecolor backcolor | ' +
                'alignleft aligncenter alignright alignjustify | ' +
                'bullist numlist outdent indent | ' +
                'link image media table | ' +
                'removeformat | code fullscreen help',

            branding: false,
            statusbar: true,

            content_style:
                'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
        });
    }