
  var tTagAft = '</div>{footer}\n{zoomCache}<p style="margin: 0 auto"><input type="date" style="margin: 5px;" name="invoice_date[]" required /></p></div>\n';
  var tBtnBrowse =  '<div class="btn btn-file btn-browse" {status} {tabIndexConfig}>{icon} {label}</div>';
        
        $(document).ready(function() {
        
        // For Invoice Upload Bulk Feature
        $(".invoice-upload-field").fileinput({
            showUpload: false,
            showClose: false,
            showRemove: true,
            theme: "explorer",
            previewMarkupTags: {
                    tagAfter: tTagAft
            },
            layoutTemplates: {
                btnBrowse: tBtnBrowse,
                main1: "{preview}\n" +
                "<div class=\'input-group {class}\'>\n" +
                "   {browse}\n" +
                "   {upload}\n" +
                "   {remove}\n" +
                "   {caption}\n" +
                "</div>"
            }
        });

        // For Financial CockPit Bulk Feature
        $(".sp-finan-cpit-upload-field").fileinput({
            showUpload: false,
            showClose: false,
            showRemove: true,
            theme: "explorer",
            layoutTemplates: {
                btnBrowse: tBtnBrowse,
                main1: "{preview}\n" +
                "<div class=\'input-group {class}\'>\n" +
                "   {browse}\n" +
                "   {upload}\n" +
                "   {remove}\n" +
                "   {caption}\n" +
                "</div>"
            }
        });

       
        
        });