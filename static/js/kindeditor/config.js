/**
 * Created by fkn on 2017/3/21.
 */
KindEditor.ready(function(K) {
                window.editor = K.create('#id_content', {
                    width: '800px',
                    height: '400px',
                    uploadJson: '/admin/upload/kindeditor',
                });
        });