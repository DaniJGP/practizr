const rowForm = document.getElementById('row-form');
const tableBody = document.getElementById('table-body');

rowForm.addEventListener('submit', (evt) => {
    evt.preventDefault();
    // Store new row values in an array
    const duration = document.getElementById('duration').value;
    const area = document.getElementById('area').value;
    const item = document.getElementById('item').value;
    const note = document.getElementById('note').value;
    const newRowData = { duration, area, item, note };

    // Validate relevant fields
    if (!duration) {
        alert('Duration is required!');
        return;
    } else if (!area) {
        alert('Area is required!');
        return;
    }


    const newRow = document.createElement('tr');
    // Iterate over object data to fill row content    
    for (const data in newRowData) {
        const newData = document.createElement('td');
        newData.textContent = newRowData[data];
        newRow.appendChild(newData);
    }

    // Add delete button
    const deleteButton = document.createElement('button');
    const deleteCell = document.createElement('td');
    deleteButton.innerHTML = 'DELETE'
    deleteButton.addEventListener('click', (evt) => {
        console.log(this.id)
    })
    deleteCell.appendChild(deleteButton);

    newRow.appendChild(deleteCell);

    // Add edit button
    const editButton = document.createElement('button');
    const editCell = document.createElement('td');
    editButton.innerHTML = 'EDIT'
    editCell.appendChild(editButton);

    newRow.appendChild(editCell);

    tableBody.appendChild(newRow);
});
