import { Injectable } from '@angular/core';
import { Task } from '../models/task.model';
import { parseCSV, stringifyCSV } from '../utils/csv';

const STORAGE_KEY = 'tasks.csv';

@Injectable({ providedIn: 'root' })
export class CsvStorageService {
  /** Read CSV string from localStorage (or empty header if not set). */
  readCsv(): string {
    const csv = localStorage.getItem(STORAGE_KEY);
    if (csv) return csv;
    const empty = 'id,title,description,dueDate,priority,status,createdAt,updatedAt';
    localStorage.setItem(STORAGE_KEY, empty);
    return empty;
  }

  /** Parse current CSV into tasks. */
  readTasks(): Task[] {
    return parseCSV(this.readCsv());
  }

  /** Persist tasks -> CSV -> localStorage. */
  writeTasks(tasks: Task[], triggerDownload = false): void {
    const csv = stringifyCSV(tasks);
    localStorage.setItem(STORAGE_KEY, csv);
    if (triggerDownload) this.downloadCsv(csv);
  }

  /** Offer a CSV file download (also available from the navbar button). */
  downloadCsv(csvText?: string, fileName = 'tasks.csv'): void {
    const csv = csvText ?? this.readCsv();
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = fileName;
    document.body.appendChild(a); a.click();
    setTimeout(() => { document.body.removeChild(a); URL.revokeObjectURL(url); }, 0);
  }
}
