function get_list(value) {
    if (value == "Technique"){
        item_list.innerHTML = '<option value="ap">AP</option><option value="dp">DP</option><option value="cc">CC</option>'
    }
    return
}

document.addEventListener('DOMContentLoaded', function() {
    let area_selected = document.querySelector('#area');
    var item_list = document.querySelector('#item');
    area_selected.addEventListener('change', function() {
        if (this.value == "technique"){
            item_list.innerHTML = '<option value="ap">AP</option><option value="dp">DP</option><option value="cc">CC</option>';
        }
    });
    }
);