// console.log('Static url_for is working!');
const rowForm = document.getElementById('row-form');
const tableBody = document.getElementById('table-body');

rowForm.addEventListener('submit', (evt) => {
    evt.preventDefault();
    // Store new row values in an array
    const duration = document.getElementById('duration').value;
    const area = document.getElementById('area').value;
    const item = document.getElementById('item').value;
    const note = document.getElementById('note').value;
    const newRowData = [ duration, area, item, note ];

    // Use array to update table contents
    const newRow = document.createElement('tr');
    newRowData.forEach( (data) => {
        const newData = document.createElement('td');
        newData.textContent = data;
        newRow.appendChild(newData);
    });
    tableBody.appendChild(newRow);
});
