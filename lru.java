import java.util.Scanner;

public class LRUPageReplacementArray {

    public static void lru(int[] pages, int capacity) {
        int[] frames = new int[capacity];
        int[] lastUsed = new int[capacity];
        int pageFaults = 0, time = 0;
        boolean isHit;

        for (int i = 0; i < capacity; i++) {
            frames[i] = -1;  // Initialize all frames to -1 (empty)
            lastUsed[i] = -1;  // Initialize all lastUsed to -1 (not used)
        }

        System.out.println("\nLRU Page Replacement:");
        System.out.println("Page No\tFrames\t\tStatus");

        for (int page : pages) {
            isHit = false;

            // Check if the page is already in one of the frames (Page Hit)
            for (int i = 0; i < capacity; i++) {
                if (frames[i] == page) {
                    isHit = true;
                    lastUsed[i] = time;  // Update the usage time
                    break;
                }
            }

            if (!isHit) {
                // Page Fault, either replace the least recently used or fill an empty frame
                int lruIndex = -1;

                // First, check if there is an empty frame
                for (int i = 0; i < capacity; i++) {
                    if (frames[i] == -1) {
                        lruIndex = i;
                        break;
                    }
                }

                // If no empty frame, find the least recently used frame
                if (lruIndex == -1) {
                    lruIndex = 0;
                    for (int i = 1; i < capacity; i++) {
                        if (lastUsed[i] < lastUsed[lruIndex]) {
                            lruIndex = i;
                        }
                    }
                }

                // Replace the LRU page
                frames[lruIndex] = page;
                lastUsed[lruIndex] = time;
                pageFaults++;
                System.out.println(page + "\t\t" + printFrames(frames) + "\tFault");
            } else {
                System.out.println(page + "\t\t" + printFrames(frames) + "\tHit");
            }

            time++;
        }
        System.out.println("Total Page Faults using LRU: " + pageFaults);
    }

    private static String printFrames(int[] frames) {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < frames.length; i++) {
            if (frames[i] != -1) {
                sb.append(frames[i]);
            } else {
                sb.append(" ");
            }
            if (i < frames.length - 1) {
                sb.append(", ");
            }
        }
        return sb.append("]").toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter number of pages: ");
        int n = scanner.nextInt();

        System.out.print("Enter reference string: ");
        int[] pages = new int[n];
        for (int i = 0; i < n; i++) {
            pages[i] = scanner.nextInt();
        }

        System.out.print("Enter number of frames: ");
        int capacity = scanner.nextInt();

        lru(pages, capacity);

        scanner.close();
    }
}
