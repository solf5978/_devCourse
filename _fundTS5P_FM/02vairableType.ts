/**
 * Varaible Declarations & Inference
 *
 */

let temperature = 79;
let humidity = 6 as 6; // Making It Literal Type

// temperature = "warm"    //   Error: Type Checking

// const humidity = 6;

const humidities = [];

temperature = 23; //  OK
temperature = humidity;
// humidity = temperature; //  NUmber is not of type 79
humidity = 6; //  6 is of type 6
// humidity = 78; //  78 is not of type 79

/**
 * let temp2 = 19; //! temp2's type is { all numbers }
 * let humid2 = 79 as const; //! humidity's type is { 79 }
 * temp2 = 23; //! Is each member in { 23 } also in { all numbers }?
 * temp2 = humid2; //! Is each member in { 79 } also in { all numbers }?
 * humid2 = temp2; //! Is each member in { all numbers } also in { 79 }?
 * humid2 = 79; //! Is each member in { 79 } also in { 79 }
 * humid2 = 78; //! Is each member in { 78 } also in { 79 }
 */

/**
 * between 500 and 1000
 * export const RANDOM_WAIT_TIME =
 *     Math.round(Math.random() * 500) + 500
 *
 * let startTime = new Date()
 * let endTime
 *
 * setTimeout(() => {
 *     endTime = 0
 *     endTime = new Date()
 * }, RANDOM_WAIT_TIME)
 */

/**
 * let frontEndMastersFounding = new Date("Jan 1, 2012")
 * let date1 = frontEndMastersFounding
 * let date2 = frontEndMastersFounding as any;
 */

const humid3 = 79 as number;
let date3 = "ooops" as any as Date;
